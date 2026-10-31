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

## Measure throughput, latency, and memory separately

Latency is how long one request takes. Throughput is how many requests or tokens can be processed per unit time. Improving throughput by batching may increase per-request latency. p50 is the median latency; p95 is the value below which 95% of requests fall. Track both under realistic concurrent traffic.

A first profiling pass measures data loading, preprocessing, model execution, and response handling. GPU utilization can be low if tokenization or disk access is the bottleneck. Memory use includes weights, activations, gradients, optimizer state, and caches. The largest memory consumer can change between training and inference.

## Quantization and mixed precision

Quantization maps values to a lower-bit representation. Weight-only quantization reduces memory; activation quantization also changes intermediate computation. Calibration data estimate ranges. Quantization-aware training exposes the model to quantization effects while learning. Test quality by task and slice, because rare-language or long-context behavior may degrade before aggregate scores.

Mixed precision uses different numeric formats for different operations. Lower precision can improve speed and memory use on supported hardware, but reductions and small gradients may need higher precision. Watch for NaNs, unstable loss, and convergence changes. Always compare with a full-precision or trusted reference.

## Distributed training and its communication costs

Data parallelism requires gradient synchronization; communication can dominate when models or networks are large. Tensor and pipeline parallelism partition computation but add coordination. Checkpointing, restart after failure, and data sharding matter in long jobs. Estimate whether a workload is large enough to justify distributed complexity.

## Worked benchmark protocol

Choose a fixed prompt set and a fixed hardware machine. Warm up the model, repeat measurements, and record model version, runtime, batch size, sequence length, precision, and concurrency. Compare baseline and quantized variants on answer quality, p50/p95 latency, peak memory, and cost per 1,000 generated tokens. Keep prompts and serving settings fixed. Do not compare a warm cache run with a cold baseline.

**Key terms:** memory bandwidth is data movement rate; compute-bound work is limited by arithmetic throughput; KV cache stores past attention states; batching groups requests; distillation trains a smaller model from a teacher; quantization reduces numerical precision.

Practice: propose a benchmark for a 7B-parameter model under a fixed device memory limit. State quality acceptance criteria before trying optimizations. Explain why fewer parameters alone does not guarantee lower latency.
