# Project 03 — Train or adapt an image classifier

## Goal

Understand image tensors, labels, convolutional or Transformer vision models, transfer learning, and class-level evaluation.

## Steps

1. Select a public dataset whose license allows your use. Write down the exact class definitions and known collection bias.
2. Display sample images and inspect dimensions, channels, intensity range, and labels.
3. Create a split that keeps images from the same person, object, video, or source together where relevant.
4. Build a simple baseline. Then train a small CNN or adapt a pretrained model; document preprocessing and augmentation.
5. Track training and validation loss. Save the best validation checkpoint, not the final epoch by default.
6. Report accuracy plus per-class precision/recall and a confusion matrix. Inspect false positives, false negatives, and difficult slices.
7. Test realistic perturbations such as lighting, blur, or background variation, and state where the model should not be used.

## Deliverables

Reproducible training/evaluation code, sample data visualization, model configuration, result table, representative error gallery with appropriate rights, and setup instructions.

## Acceptance checks

Labels remain aligned after resize/crop/augmentation; test images did not leak from training sources; the baseline is shown; and claims match the evidence.

## Stretch

Compare frozen-feature extraction with partial fine-tuning. Measure latency and memory on the hardware you intend to use.