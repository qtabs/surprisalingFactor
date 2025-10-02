import llama_cpp
import numpy as np
import os
import scipy.special
import time
from tqdm import tqdm

class Lamoid():
	
	def __init__(self, model_path, max_tokens=2048, n_top_probs=2048, gpu=False):

		model_path = os.path.abspath(os.path.expanduser(model_path))
		self.model = llama_cpp.Llama(model_path=model_path,
						    		 n_ctx=max_tokens,
						    		 n_gpu_layers=(-1 if gpu else 0),
						     		 logits_all=True,
						     		 verbose=False)

		self.max_tokens  = max_tokens
		self.model_path  = model_path
		self.vocabulary_size = self.model.n_vocab()

		# Validate n_top_probs
		if n_top_probs > self.vocabulary_size:
			raise ValueError(f"n_top_probs ({n_top_probs}) cannot exceed vocabulary size ({self.vocabulary_size})")

		self.n_top_probs = n_top_probs 

	def predict_next_word(self, input_list):

		# Trim the input in token space to match max_tokens:
		input_str = ' '.join(input_list)

		tokens = self.model.tokenize(input_str.encode("utf-8"))

		if len(tokens) >= self.max_tokens:
		    tokens = tokens[-(self.max_tokens-2):]  # keep last part

		input_str = self.model.detokenize(tokens).decode("utf-8", errors="ignore")

		# Run the model
		model_out = self.model.create_completion(input_str, 
											  	 max_tokens=1, 
											  	 logprobs=self.n_top_probs)

		log_probs = model_out['choices'][0]['logprobs']['top_logprobs'][0]
		
		return log_probs

	def compute_next_word_logprob(self, input_list, next_word):

		log_probs = self.predict_next_word(input_list)

		# Check if the next_word appears in the returned tokens
		# Note: next_word might be split into multiple tokens by the tokenizer
		found = False
		for token_str in log_probs.keys():
			# Strip whitespace for comparison since tokens may have leading spaces
			if token_str.strip() == next_word.strip() or token_str == next_word:
				logp = log_probs[token_str]
				found = True
				break

		if not found:
			logp = self._approximate_logp_of_unassigned_word_(log_probs)

		return logp

	def _approximate_logp_of_unassigned_word_(self, log_probs):
		
		# if word is not included in top_k, we approximate the logp so that 
		# p_word ~ (1 - sum_(top_k) p) / (vocabulary_size - k)
		
		assigned_logp = scipy.special.logsumexp(list(log_probs.values()))

		# Stable estimation of unassigned log probability
		if assigned_logp < np.log(2.0):
			unassigned_logp = np.log1p(-np.exp(assigned_logp))
		else:
			unassigned_logp = np.log(-np.expm1(assigned_logp))

		unassigned_vocabulary_size = self.vocabulary_size - self.n_top_probs
		logp = unassigned_logp - np.log(unassigned_vocabulary_size)

		return logp



model_path = '~/Documents/Models/llama31-8b/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf'
paper_path = './examples/dummy_neuro_article.txt'

with open(paper_path, 'r') as f:
	paper_content = f.read().split()[:100]


llm = Lamoid(model_path, max_tokens=256, n_top_probs=128, gpu=True)

t0 = time.time()
logp = np.empty(len(paper_content))
logp[0] = np.nan  # First word has no context
for t in tqdm(range(1, len(paper_content))):
	logp[t] = llm.compute_next_word_logprob(paper_content[:t], paper_content[t])

tt = (time.time()-t0)


print(f'time = {tt:.2f} seconds')
#print(f'gpu time = {tt_gpu:.2f}seconds')
