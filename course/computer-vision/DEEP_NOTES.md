# Computer vision — full beginner notes

Computer vision uses images or video as data. A model does not receive “a picture” as humans experience it; it receives arrays of numeric pixel values, possibly transformed into learned features.

## 1. Pixels, tensors, convolutions, and CNNs

A grayscale image is a grid of intensity values. A color image commonly has height, width, and channel axes for red, green, and blue. A batch adds another axis. Pixel values may use integer ranges or be converted to floating point and normalized. Inspect shape, channel order, value range, orientation, and label alignment; these are frequent sources of silent errors.

A **convolution** applies a small learned filter across an image. At each location, filter values multiply nearby pixels and sum to produce a feature map. Early filters may respond to edges or color transitions; later layers combine local patterns. The filter is shared across positions, reducing parameters and responding to local patterns wherever they occur.

**Stride** controls how far the filter moves; **padding** adds border values to control output size; **kernel** is the filter window; **channel** is one feature plane. **Pooling** downsamples a feature map, often by taking a local maximum or average. A **CNN** is a neural network that uses convolutional operations, usually combined with activation, pooling, and final classification layers.

A tiny example: a 3×3 filter slides across a 5×5 grayscale image. At each valid location, it sees 9 pixels, computes a weighted sum, and writes one output value. The same 9 learned weights are reused at every location. This reuse is **parameter sharing**.

## 2. Vision tasks, transfer, and evaluation

**Image classification** assigns one or more labels to a whole image. **Object detection** predicts boxes and classes. **Semantic segmentation** labels each pixel by class; **instance segmentation** also distinguishes separate objects of the same class. **Keypoint estimation** predicts landmark coordinates. Video tasks add a time dimension and motion.

A dataset needs consistent annotation rules. For bounding boxes, specify whether coordinates are normalized or measured in pixels. Image resizing and cropping must transform labels too. Augmentation such as horizontal flips is valid only when it preserves the label; flipping text or asymmetric medical images may change meaning.

Transfer learning starts from a pretrained vision model. First freeze the feature extractor and train a small classifier, then consider fine-tuning. Compare against a baseline and inspect per-class confusion. **Intersection over Union (IoU)** measures overlap between predicted and true boxes or masks. **Mean Average Precision (mAP)** summarizes precision-recall behavior across classes and thresholds; precise definitions depend on the benchmark.

A high aggregate score may hide poor performance on small objects, low light, rare classes, or particular camera sources. Split by subject, site, or time when related images could leak across train and test. Evaluate on representative images and inspect errors in original context.

### Q&A and practice

**Why use convolution instead of a dense layer on every pixel?** Local filters share weights across positions and preserve spatial structure with fewer parameters.
**Can I augment images freely?** No. A transformation is safe only when the task label remains valid.
**What should I report?** Dataset source, label rules, split, preprocessing, metric, class-level errors, and limitations.

Practice: display a sample tensor, plot its channels, manually calculate one convolution window, train a pretrained model on a small dataset, and inspect false positives and negatives. Continue to [deep learning](../deep-learning/README.md).