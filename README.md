# NRSC-KG

NRSC-KG: Noise-Robust Speech Comprehension Based on Knowledge Graph for HRI
Speech comprehension is the key to Human-Robot Interaction (HRI), however, noise energetic masking can greatly reduce the performance of speech comprehension. Simply using Speech Enhancement (SE) methods can easily lead to suboptimal solutions. To alleviate these issues, this paper proposes a Noise-Robust Speech Comprehension system based on Knowledge Graph (NRSC-KG), which designs robust methods in Automatic Speech Recognition (ASR) and ASR error correction. In ASR, we propose a Self-adaptive Speech Feature Fusion Network (SSFF-Net) to dynamically fuse enhanced speech features with the original speech features. In ASR error correction, we propose a divergent apperceive error correction method based on domain-specific Knowledge Graph (KG). The experiment on AISHELL-1 speech corpus shows that compared to the traditional joint training of SE and ASR, our  method achieves a relative Character Error Rate (CER) reduction of 12.7%. We validated the KG based  error correction method on our customized Herbal Cuisine ordering Dialogue  speech dataset (HCDialogue), and the results showed that our method achieved a relative CER reduction of 5.0% and 2.1%, respectively, compared to the language model based and end-to-end neural network based methods. It’s indicated that the KG based method has great potential in improving speech comprehension performance.



The main implementation code of the Self-adaptive Speech Feature Fusion Network (SSFF-Net) part is in espnet_model.py and fusion.py.This part of the experiment was implemented on the espnet framework

The main implementation code of the divergent apperceive error correction method based on domain-specific Knowledge Graph (KG) part is in Mac+neo4j.py,corrector.py,detector.py and neo4j.py.This part of the experiment was implemented on the pycorrector framework.
