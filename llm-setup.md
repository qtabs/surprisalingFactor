Warning! This is an AI-generated guide, things might be wrong here. I followed this post to install llama-cpp with metal support in Mac and it works:

https://medium.com/@akdemir_bahadir/how-to-build-and-install-llama-cpp-python-on-apple-silicon-without-losing-your-mind-96d186f86d73

For other platforms, follow what's next with caution ^^.


# Local LLM Setup Guide (macOS, Linux, Windows)

This guide explains how to install [llama.cpp](https://github.com/ggerganov/llama.cpp), set up Hugging Face, download models into a `models` folder, run them from CLI and Python, and enable GPU acceleration.

---

## 1. Install Dependencies

### macOS
Make sure you have **Homebrew** installed. If not:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install tools:
```bash
brew install cmake git python
```

---

### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install -y build-essential cmake git python3 python3-pip
```

If you have an NVIDIA GPU, also install CUDA toolkit:
```bash
sudo apt install -y nvidia-cuda-toolkit
```

---

### Windows
1. Install **Git for Windows**: [https://git-scm.com/download/win](https://git-scm.com/download/win)  
2. Install **CMake**: [https://cmake.org/download/](https://cmake.org/download/)  
3. Install **Python**: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)  
4. Install **Visual Studio Build Tools** (with C++ build tools).  
5. For GPU acceleration: install **CUDA Toolkit** (if NVIDIA GPU) or enable **DirectML** (for AMD/Intel).  

---

## 2. Install `llama.cpp`

Clone and build:

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
make
cd ..
```

---

## 3. Enable GPU Acceleration

### macOS (Metal)
Build with Metal acceleration:
```bash
cd llama.cpp
make clean && LLAMA_METAL=1 make
cd ..
```

Run with Metal backend:
```bash
./llama.cpp/main -m ./models/llama31-8b/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf --gpu-layers 50 -p "Hello!"
```

---

### Linux (CUDA)
Build with CUDA:
```bash
cd llama.cpp
make clean && LLAMA_CUBLAS=1 make
cd ..
```

Run with CUDA backend:
```bash
./llama.cpp/main -m ./models/llama31-8b/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf --gpu-layers 50 -p "Hello!"
```

---

### Windows (CUDA / DirectML)
- CUDA (NVIDIA):
```powershell
cmake -S . -B build -DLLAMA_CUBLAS=ON
cmake --build build --config Release
```

- DirectML (AMD/Intel):
```powershell
cmake -S . -B build -DLLAMA_DML=ON
cmake --build build --config Release
```

Run:
```powershell
.uildin\Release\main.exe -m .\models\llama31-8b\Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf --gpu-layers 50 -p "Hello!"
```

---

## 4. Install Hugging Face CLI

```bash
pip install --upgrade huggingface_hub
```

Check:
```bash
hf --help
```

---

## 5. Create a Hugging Face Account

1. Go to [https://huggingface.co/join](https://huggingface.co/join)  
2. Verify your email  
3. (Required for LLaMA) Accept Meta’s license at [Meta LLaMA model card](https://huggingface.co/meta-llama)  

---

## 6. Log In to Hugging Face

```bash
huggingface-cli login
```

Paste in your **access token** from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

---

## 7. Download Models into `models/`

Run this:

```bash
mkdir -p models && cd models

mkdir -p llama31-8b && hf download bartowski/Meta-Llama-3.1-8B-Instruct-GGUF   --include "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"   --include "Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf"   --local-dir ./llama31-8b && mkdir -p qwen25-7b && hf download bartowski/Qwen2.5-7B-Instruct-GGUF   --include "Qwen2.5-7B-Instruct-Q4_K_M.gguf"   --include "Qwen2.5-7B-Instruct-Q5_K_M.gguf"   --local-dir ./qwen25-7b && mkdir -p mistral-7b && hf download TheBloke/Mistral-7B-Instruct-v0.2-GGUF   --include "mistral-7b-instruct-v0.2.Q4_K_M.gguf"   --include "mistral-7b-instruct-v0.2.Q5_K_M.gguf"   --local-dir ./mistral-7b
```

This creates:
```
models/
  ├── llama31-8b/
  ├── qwen25-7b/
  └── mistral-7b/
```

---

## 8. Run Models with `llama.cpp`

Example (LLaMA 3.1 8B Q4_K_M):

```bash
./llama.cpp/main -m ./models/llama31-8b/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf -p "Hello, how are you?"
```

With GPU layers (faster):
```bash
./llama.cpp/main -m ./models/llama31-8b/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf --gpu-layers 50 -p "Hello, how are you?"
```

---

## 9. Call Models from Python

Install Python bindings:

```bash
pip install llama-cpp-python
```

Example script (`run_model.py`):

```python
from llama_cpp import Llama

# Load model
llm = Llama(
    model_path="./models/llama31-8b/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
    n_gpu_layers=50  # use GPU acceleration if available
)

# Run prompt
output = llm("Q: What is the capital of France? A:")

print(output["choices"][0]["text"])
```

Run:
```bash
python run_model.py
```

---

# ✅ Done

You now have:
- `llama.cpp` installed with GPU acceleration  
- Hugging Face CLI set up  
- Models downloaded to `models/`  
- Working CLI and Python examples  





