# Caribbean Voices ASR Hackathon

Automatic Speech Recognition model for Caribbean accents - Zindi Competition

## Team

- **Chad**: Modeling Lead - ASR model development & fine-tuning
- **Donahue**: Infrastructure Lead - Data pipeline, preprocessing, GPU setup
- **Elroy**: Strategy Lead - Error analysis, submissions, Phase 2 pitch

## Competition Info

- **Platform**: [Zindi Competition Link]
- **Deadline Phase 1**: December 7, 2025
- **Deadline Phase 2**: December 13, 2025
- **Evaluation**: Word Error Rate (WER)

## Quick Start

### Setup

```bash
# Clone repo
git clone <repo-url>
cd caribbean-asr-hackathon

# Install dependencies
pip install -r requirements.txt

# Download data (see data/README.md)
```

### Project Structure

- `data/`: Dataset and splits (gitignored, see README for download)
- `notebooks/`: Exploratory analysis and experiments
- `src/`: Shared code (preprocessing, models, evaluation)
- `experiments/`: Experiment tracking (experiments.csv)
- `submissions/`: Generated submission files

## Workflow

### Branch Strategy

- `main`: Stable, working code only
- `dev`: Integration branch
- `feature/<name>-<description>`: Individual work

Example: `feature/chad-whisper-lora`, `feature/donahue-noise-reduction`

### Making Changes

1. Create feature branch from `dev`
2. Make your changes
3. Test locally
4. Push and create PR to `dev`
5. One teammate approves
6. Merge to `dev`
7. Periodically merge `dev` → `main` for stable checkpoints

### Experiment Tracking

Log all experiments in `experiments/experiments.csv`:

```csv
exp_id,date,person,model,preprocessing,config,val_wer,public_lb,notes,commit_hash
001,2024-11-21,donahue,baseline,none,default,0.250,-,Whisper-large-v3 zero-shot,abc123
```

See `experiments/README.md` for details.

## Communication

- **Daily Standup**: 7 PM EST in WhatsApp group
- **Sync Meetings**: Mon/Thu 7 PM EST (30 min)
- **Blockers**: Tag in WhatsApp immediately

## Resources

- [Competition Page](https://zindi.africa/competitions/...)
- [Experiment Tracker](experiments/experiments.csv)
- Hostinger GPU Access: [Details in docs/setup_instructions.md]
- [Whisper Documentation](https://github.com/openai/whisper)

## Current Status

- [x] Team formed
- [x] Repo setup
- [ ] Data downloaded
- [ ] Baseline model run
- [ ] Train/val split created
- [ ] First submission

## Week 1 Goals

**Days 1-2 (Thu-Fri)**
- Donahue: Data exploration, quality assessment
- Chad: Whisper baseline (zero-shot)
- Elroy: Evaluation framework, metrics tracking

**Days 3-4 (Sat-Sun)**
- All: Review findings, decide split strategy
- Donahue: Create train/val/holdout splits
- Chad: Start fine-tuning
- Elroy: Baseline error analysis

**Days 5-7 (Mon-Wed)**
- Chad: Hyperparameter experiments
- Donahue: Preprocessing pipeline
- Elroy: Leaderboard strategy, error patterns
- Target: First submission by Wednesday

---

Last updated: November 21, 2024
