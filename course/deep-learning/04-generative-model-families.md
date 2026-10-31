# Deep learning: generative model families

> **Place in the course:** Optional theory after neural networks and probability. Generative AI is not one architecture; model families represent and sample data differently.

## What is generation?

A generative model learns aspects of a data distribution and samples new examples. It may estimate an explicit likelihood, use latent variables, or generate plausible samples without a tractable likelihood. A realistic-looking output is not necessarily diverse, factual, safe, or representative.

## Autoregressive models

An autoregressive model factorizes a sequence probability into next-step probabilities: each item is predicted from earlier items. Language models predict the next token; image models can predict pixels or patches in an order. Sampling is straightforward, but generation is sequential and can be slow.

## Variational autoencoders

A variational autoencoder (VAE) maps an example to a distribution over latent variables, samples a latent code, and decodes it. Its objective balances reconstruction and a regularizer that keeps latent distributions near a prior. The evidence lower bound enables approximate learning.

Latent variables can support interpolation and compact representations. A strong regularizer may cause the decoder to ignore them, called posterior collapse. VAEs are useful for probabilistic representations, even when generated samples look smoother than adversarial outputs.

## Generative adversarial networks

A GAN trains a generator to create samples and a discriminator to distinguish generated samples from real ones. Their objectives compete. GANs can produce sharp samples but training can be unstable. **Mode collapse** occurs when output diversity is low even though some samples fool the discriminator. Evaluate coverage as well as apparent quality.

## Diffusion models

Diffusion training gradually adds noise and teaches a network to predict or remove it. Sampling begins from noise and applies repeated denoising. This can create diverse high-quality samples, but standard generation requires multiple model calls. Latent diffusion runs the process in a compressed representation to reduce computation. Guidance can trade diversity for following conditioning more closely.

## Flows and model selection

Normalizing flows transform a simple distribution through invertible functions and compute exact density using a change-of-variables formula. Invertibility and Jacobian calculations constrain architecture. Flows are useful when likelihood matters, with compute trade-offs.

Choose by task: likelihood, sample quality, diversity, controllability, speed, training stability, and data type. A model family does not replace evaluation.

**Questions:** Why can a GAN collapse? It may exploit the discriminator without covering the data. Why can diffusion be slower? Generation often requires repeated denoising. Why use a VAE latent distribution? It enables approximate inference over hidden factors.

**Practice:** Compare autoregressive, VAE, GAN, diffusion, and flow models by learning objective, sampling process, strength, and limitation. Choose one for a stated application.

Further reading: [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114), [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661), and [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239).
