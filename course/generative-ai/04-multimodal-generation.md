# Chapter 4 — Image, audio, and video generation

## Diffusion intuition

A diffusion model gradually adds noise to training examples and learns to reverse that corruption. During generation, it starts from noise and applies repeated denoising steps conditioned on text or another signal. The [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) paper is a foundational formulation.

Generation quality depends on training data, conditioning, architecture, sampling steps, and guidance. A prompt is not a guarantee that a requested concept is represented faithfully.

## Audio and speech

Audio can be represented as a waveform or time-frequency features. Speech recognition maps sound to text; text-to-speech maps text to generated speech; audio generation may create music or sound effects. Voice likeness and speech content raise consent, impersonation, and provenance concerns.

## Video and multimodal systems

Video adds temporal continuity. A system may generate each frame plausibly while objects flicker or change identity over time. Multimodal models combine text, images, audio, or video representations, but each modality has its own preprocessing and evaluation.

## Questions and answers

**Does diffusion simply remove noise?**  
It learns a sequence of denoising transformations under a training objective. Sampling approximates a process that produces structured outputs from noise.

**Why can a generated video look inconsistent?**  
Frame-level quality does not guarantee temporal consistency. Identity, physics, lighting, and movement need separate evaluation.

**What should be considered before generating a real person's voice or image?**  
Consent, rights, disclosure, misuse risks, and safeguards against impersonation.

## Practice and mastery

Generate a small set of images with controlled prompt variations. Compare prompt adherence, artifacts, diversity, and bias. For audio or video, add a temporal or identity-consistency check instead of judging only one frame.