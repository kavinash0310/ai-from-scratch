# Chapter 1 — Images, convolution, and computer vision networks

## An image is a tensor

A grayscale image is a grid of intensity values. A color image commonly has height, width, and channel dimensions. A dataset adds a batch dimension. Pixel values may be normalized, but transformations must be learned or applied consistently.

Image preprocessing includes resize/crop, channel ordering, normalization, and augmentation. A mismatch between training and inference preprocessing can cause large quality loss.

## Convolution

A convolutional filter slides across an image and computes local weighted sums. Early filters can respond to simple patterns such as edges or textures. Later layers combine local responses into larger patterns.

Stride controls step size; padding controls edge treatment; kernel size sets the local receptive field. Pooling or strided convolution reduces spatial resolution. Convolution shares weights across locations, which helps exploit local structure.

## Modern image models

CNNs use local convolutional operations. Vision transformers split images into patches and process them with attention. Residual blocks add a block's input to its transformed output, supporting deep networks. The [ResNet paper](https://arxiv.org/abs/1512.03385) introduces residual learning.

Architecture choice depends on data, latency, resolution, available pretrained models, and deployment hardware. Use small inputs and models while learning.

## Questions and answers

**Why do CNNs share weights?**  
The same filter can detect a pattern at different image locations, reducing parameters and reflecting spatial locality.

**What is a receptive field?**  
The input region that can influence one output unit. It grows as layers and strides combine.

**Why does normalization matter?**  
It makes input scales more consistent with training assumptions. Incorrect inference normalization changes the distribution seen by the model.

**Are vision transformers always better than CNNs?**  
No. Data size, pretraining, compute, architecture, and task determine performance.

## Practice and mastery

Inspect a small image tensor's shape and range. Apply a convolution filter to a tiny grayscale image by hand or with a library. Explain how kernel size, stride, and padding affect output dimensions.