# DL-PINNs

This project has been developed by Luís Freire, Tiago Silvério, Bartholomeus Pepping, Jacon Schlander for the course Deep Learning at DTU.

This project was made as an exploration of the applications of physics-informed neural networks (PINNs) in approximating and adapting to known physical problems. The primary focus was on understanding how these deep learning models could effectively address such problems. PINNs were particularly emphasized due to their capability to achieve accurate approximations while requiring relatively minimal datasets.

To demonstrate their efficacy in approximating a small-scale wave problem derived from fluid dynamics, a PINN was specifically formulated and contrasted against a purely data-driven approach using an identical feed-forward neural network architecture to the PINN. The comparison revealed a substantial reduction in the required data points for the PINN compared to the purely data-driven model, coupled with superior performance in yielding more accurate results. Furthermore, the adaptability of the PINN was notably demonstrated when accommodating the introduction of a body into the water scenario.

Contents:
- **ModelWithBody**: notebook for the Model with Body, containing the pre-trained model and the two implementations
- **FinetunedModel**: notebook for the fine tuned model, containing the comparison between w/ and w/o SoftAdapt
- **DataDrivenModel**: notebook with a model following a data-driven for comparison with our model
