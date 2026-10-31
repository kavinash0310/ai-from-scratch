# AI engineering: efficient training and inference

> **Place in the course:** Advanced implementation study. Optimize only after building a valid baseline and evaluation.

## Measure the actual bottleneck

Training and inference consume compute, memory, storage, bandwidth, and energy. GPUs excel at parallel tensor operations, but small workloads may not use them efficiently. Some operations are compute-bound; others wait on memory or input data. Profile end-to-end time before changing the model.

Training memory includes weights, gradients, optimizer state, and saved activations. A large batch may exceed device memory. Gradient accumulation performs several small batches before an update, but changes optimization noise and is not always identical to one large batch. Activation checkpointing recomputes some values during backpropagation, saving memory at extra compute.

## Precision and quantization

Float32, float16, and bfloat16 offer different precision and numeric range. Mixed precision uses lower precision where hardware supports it while keeping selected operations stable. Verify loss behavior and evaluation against a reference.

Quantization stores or computes weights with fewer bits, which may reduce memory and latency. It can change quality. Post-training quantization is applied to a trained model; quantization-aware training simulates quantization effects during training. Hardware and runtime determine whether lower-bit arithmetic actually speeds the system.

## Inference optimizations

Batching improves throughput but can increase wait time for an individual request. KV caching avoids recomputing earlier attention states, trading memory for speed. Distillation trains a smaller student to imitate a larger teacher. Pruning removes weights, but sparse weights help only if the runtime and hardware exploit them. Speculative decoding uses a draft model to propose tokens that a larger model verifies.

Compare variants on the same evaluation: quality, p50 and p95 latency, memory, throughput, and cost per request. Define an acceptable quality-loss threshold first.

## Distributed training

Data parallelism runs model replicas on different examples and synchronizes gradients. Tensor parallelism splits large operations across devices. Pipeline parallelism assigns different layers to stages. These methods introduce communication and synchronization costs; more GPUs do not always mean lower runtime or cost.

Beginners should first profile a small workload and understand the data path, device memory, and reproducibility. Then change one optimization and compare.

**Questions:** Does quantization always improve speed? No; hardware and software support matter. Why measure p95 latency? Averages hide slow-tail user experiences. Why not optimize first? Without a baseline, quality loss is unknown.

**Practice:** Benchmark one model with two batch sizes and two precisions. Record hardware, warm-up, median and p95 latency, peak memory, and quality. State your stopping rule.

Further reading: [NVIDIA performance guide](https://docs.nvidia.com/deeplearning/performance/dl-performance-getting-started/index.html) and [mixed-precision guide](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html).
