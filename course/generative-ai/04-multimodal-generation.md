# Chapter 4 — Image, audio, and video generation

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Diffusion intuition

A diffusion model gradually adds noise to training examples and learns to reverse that corruption. During generation, it starts from noise and applies repeated denoising steps conditioned on text or another signal. The [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) paper is a foundational formulation.

Generation quality depends on training data, conditioning, architecture, sampling steps, and guidance. A prompt is not a guarantee that a requested concept is represented faithfully.

## Audio and speech

Audio can be represented as a waveform or time-frequency features. Speech recognition maps sound to text; text-to-speech maps text to generated speech; audio generation may create music or sound effects. Voice likeness and speech content raise consent, impersonation, and provenance concerns.

## Video and multimodal systems

Video adds temporal continuity. A system may generate each frame plausibly while objects flicker or change identity over time. Multimodal models combine text, images, audio, or video representations, but each modality has its own preprocessing and evaluation.

## Deeper walkthrough: diffusion sampling

During training, a clean image x₀ is gradually mixed with noise at a chosen timestep t. The model receives the noisy sample and timestep, then learns to predict the noise or another parameterization of the reverse process. At generation, begin with random noise and apply repeated denoising steps conditioned on text.

Fewer sampling steps can reduce time but may reduce fidelity; guidance strength changes prompt adherence and diversity. These are tradeoffs to evaluate, not universal settings.

Image evaluation should look at prompt alignment, artifacts, diversity, and harms such as stereotyped depictions. Audio additionally needs intelligibility and speaker/consent checks; video needs temporal consistency. Human reviewers need a rubric because “looks good” is not reproducible.

Generated media should be clearly disclosed where users could mistake it for authentic evidence.

## Questions and answers

**Does diffusion simply remove noise?**  
It learns a sequence of denoising transformations under a training objective. Sampling approximates a process that produces structured outputs from noise.

**Why can a generated video look inconsistent?**  
Frame-level quality does not guarantee temporal consistency. Identity, physics, lighting, and movement need separate evaluation.

**What should be considered before generating a real person's voice or image?**  
Consent, rights, disclosure, misuse risks, and safeguards against impersonation.

## Practice and mastery

Generate a small set of images with controlled prompt variations. Compare prompt adherence, artifacts, diversity, and bias. For audio or video, add a temporal or identity-consistency check instead of judging only one frame.