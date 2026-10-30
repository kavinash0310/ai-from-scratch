# Computer vision
## A beginner's textbook chapter

Computer vision turns images and video into machine-readable representations for recognition, measurement, tracking, or generation. A vision model receives arrays of numbers, not the image as a human experience. Correct data shape and label handling are essential.

## 1. An image as a tensor

A grayscale image can be represented as height by width, where each value is pixel intensity. A color image adds a channel axis for red, green, and blue. A batch adds a batch axis. Libraries may expect channel-first or channel-last order, so inspect shapes rather than guessing.

Pixels may be stored as integers from 0 to 255 or floating values. Normalization rescales them, often to 0–1 or to a standardized range. Preprocessing must be identical between training and inference. Resizing, cropping, or rotating images can change where an object is; bounding boxes or masks must receive the same transformation.

## 2. Convolution and shared filters

A convolution-like operation applies a small kernel to local image neighborhoods. At each position, multiply nearby pixels by kernel weights and sum them into an output feature. The same weights are reused over the image. This is **parameter sharing** and builds in the assumption that a useful local pattern can occur at different positions.

A 3 by 3 kernel contains nine weights. On a 5 by 5 image with no padding and stride one, the output dimensions are 3 by 3 because the kernel can begin at rows 0, 1, 2 and columns 0, 1, 2. **Stride** is how far the kernel moves. **Padding** adds border values and controls output size. **Channels** represent separate input or learned feature planes.

In many deep learning libraries, an operation called convolution is mathematically cross-correlation: the kernel is not flipped. This implementation convention does not prevent learning because the kernel values are learned.

Early layers can respond to edges or color transitions. Later layers combine patterns. A feature map is a spatial pattern of activations, not an explanation by itself.

## 3. CNN architecture

A **convolutional neural network (CNN)** commonly stacks convolution, activation, and sometimes pooling or normalization. Pooling or strided convolution reduces spatial dimensions. Later features are aggregated for classification, detection, or segmentation.

A dense layer connected to every raw pixel has many weights and ignores the image's local structure. Convolution exploits locality and reuses weights. **Receptive field** means the portion of the original image that can influence a unit; it grows as layers combine nearby features.

Residual networks add a shortcut that sums a block input with a transformed output. This gives signals and gradients a more direct route through deep networks. Pretrained ResNets are often useful baselines for small image datasets.

## 4. Vision tasks

- **Image classification:** one or more labels for a whole image.
- **Object detection:** labels plus location, often bounding boxes.
- **Semantic segmentation:** a class label for each pixel.
- **Instance segmentation:** pixel masks that distinguish separate objects of the same class.
- **Keypoint estimation:** coordinates of important landmarks.
- **Tracking:** link detected objects over time in video.

Each task needs annotation rules. A box convention must define coordinate origin, units, and whether edges are inclusive. Ambiguous labels create a noisy training target.

## 5. Transfer and evaluation

When labels are limited, start with a pretrained model. Freeze its feature extractor and train a small head. If validation shows gains, unfreeze selected layers. Avoid tuning on the final test set.

For classification, report per-class precision and recall, not only accuracy. For boxes or masks, **Intersection over Union (IoU)** measures overlap. **Mean Average Precision (mAP)** summarizes precision-recall performance across classes or overlap thresholds; the exact benchmark definition varies.

Avoid leakage: images of the same person, object, video, or source can be near-duplicates. Split by person/site/time when that matches intended deployment. Examine low light, blur, small objects, and rare classes. Image augmentation is valid only if it preserves the label; horizontal flips are wrong for text or asymmetric medical scans.

## 6. Worked example: classify handwritten digits

A simple project can classify 8 by 8 grayscale digit images. First display a batch and check that each label aligns with its image. Normalize intensities. Compare a majority-class baseline with a logistic model or small neural network. Use a stratified split so each digit appears in both training and test sets. Inspect a confusion matrix: confusing 3 and 8 may be reasonable; systematically confusing one digit with another might reveal a preprocessing or label issue.

This project demonstrates classification, but not production readiness. Handwritten digits are simpler than noisy documents, medical images, or images from changing cameras.

## 7. Questions and exercises

**Why does a CNN share kernel weights?** A useful local pattern can appear in different image locations, so the same detector can be reused.

**Why is resizing not just a storage choice?** It can distort shapes and requires corresponding changes to spatial labels.

**Does a high test accuracy prove robust vision?** No. The test distribution may omit lighting, camera, or subgroup conditions that matter.

Exercise: use the [convolution lab](../../labs/computer-vision/08_convolution.py). Predict its output shape before running it; then flip the kernel and explain the sign change. Continue to the [deep-learning textbook](../deep-learning/README.md).