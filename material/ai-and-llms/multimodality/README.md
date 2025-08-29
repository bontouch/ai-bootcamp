# Multimodality

## Session 1
This first session presents a python notebook explaining how multimodal LLM API's are capable of not just analyzing text, but also images. We also touch upon audio transcription and how that opens up new capabilities to process audio data with LLMs.

The final example in the notebook is a simplification of an experiment made with Swish payments. It shows how a video can be split up into text and images in order to parse it into an URL.

## Session 2

In session 2 we explore image embeddings—just like text embeddings, but for images. They let us measure similarity between images and search a database of Systembolaget products for visually similar matches.

Since raw embeddings tend to not be so accurate (e.g. two images may look alike simply because both show a bottle or a similar label), we use GPT-4.1 with vision to reason about the results and decide whether the candidates are actually the same product.
