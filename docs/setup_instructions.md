# Setup Instructions

## Initial Setup

### 1. Clone Repository

```bash
git clone https://github.com/elroy-galbraith/caribbean-asr-hackathon.git
cd caribbean-asr-hackathon
```

### 2. Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Download Data

See `data/README.md` for instructions.

### 4. Hostinger GPU Access

**Server details**: [Donahue to fill in]

```bash
# SSH into Hostinger
ssh root@31.97.40.116
Password:#PGMS@19-6JAm

# Check GPU
CPU Core 2
Memory 8 gb
Disk Space 100 gb

nvidia-smi

# Install dependencies on server
pip install -r requirements.txt
```

## Development Workflow

### Running Experiments Locally

```bash
# Test on sample
python src/models/whisper_finetune.py --config config/training_config.yaml --test-run

# Full training
python src/models/whisper_finetune.py --config config/training_config.yaml
```

### Running on Hostinger

```bash
# Transfer code
rsync -avz --exclude 'data/' --exclude '.git/' . username@server:/path/to/project/

# SSH and run
ssh root@31.97.40.116
cd /path/to/project
python src/models/whisper_finetune.py --config config/training_config.yaml
```

### Jupyter Notebooks

```bash
# Start locally
jupyter notebook

# Or use Jupyter on Hostinger (port forwarding)
ssh -L 8888:localhost:8888 username@server
# On server:
jupyter notebook --no-browser --port=8888
# Access at localhost:8888 in your browser
```

## Troubleshooting

**Import errors:**

```bash
pip install -e .  # Install package in editable mode
```

**CUDA out of memory:**

- Reduce batch size
- Use gradient checkpointing
- Try smaller model (whisper-medium)

**Audio loading issues:**

```bash
# Install ffmpeg
# Mac:
brew install ffmpeg
# Ubuntu:
sudo apt-get install ffmpeg
```

## Team-Specific Notes

**Chad**: [Modeling-specific setup]  
**Donahue**: [Infrastructure access details]  
**Elroy**: [Strategy tools setup]

---

Last updated: November 20, 2024
