# Chapter 2 — Vision tasks, transfer, and evaluation

## Match labels to the task

- Classification assigns one or more labels to an image.
- Object detection predicts categories and bounding boxes.
- Segmentation predicts a category for each pixel or region.
- Tracking links objects across video frames.
- Generation creates or edits images.

The label format differs for each task. Image-level labels cannot train accurate boxes without additional annotation. Segmentation needs masks. Clarify if multiple objects or labels can appear.

## Transfer learning and data splits

Pretrained vision encoders can reduce training needs. Fine-tune carefully and compare against a simple baseline. Split by source, photographer, patient, location, or video sequence where correlated images could otherwise leak across train and test.

Near duplicates can create inflated test scores. Check for them before reporting results.

## Evaluate the actual use

Classification may need per-class precision and recall; detection uses overlap and matching rules; segmentation measures overlap per class. Average scores can hide rare-class failure. Inspect misclassified examples and group errors by lighting, resolution, occlusion, background, and source.

A model that recognizes a background shortcut may score well while failing on new environments. Test controlled variations and locations relevant to deployment.

## Questions and answers

**Why can image-level train/test splitting be misleading?**  
Images from the same person, scene, or video can appear in both sets, letting the model benefit from near-duplicates.

**What is a shortcut feature?**  
A pattern correlated with the label in training but not reliably connected to the target, such as a background watermark.

**Why inspect individual errors?**  
Aggregate metrics reveal scale; examples reveal mechanisms such as label noise, blur, cropping, or class ambiguity.

**What does transfer learning reuse?**  
Parameters or representations from a model trained on another dataset. The new task still requires appropriate labels and held-out evaluation.

## Practice and mastery

Build an image classifier with a simple baseline and a pretrained model. Split by image source if possible, report per-class metrics, inspect at least 20 errors, and document what conditions remain untested.