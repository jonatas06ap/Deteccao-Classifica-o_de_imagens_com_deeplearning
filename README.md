# Deteccao-Classifica-o_de_imagens_com_deeplearning
Foi feito uma rede de Deep Learning para detectar duas classes de objetos, duas pelúcias. 


O dataset foi criado aplicando a partir de 89 imagens, as quais foram dividas em:  
1. Treino: 50 imagens originais + 100 criadas com Data Augmentation (Shear, Flip e Rotation) (yolo3/dataset/train)
2. Validação: 25 imagens (yolo3/dataset/valid)
3. Teste: 25 imagens (yolo3/dataset/test)

A rede usada como base foi a YOLOv3, usada a partir do Framework PyTorch e placa de vídeo
Nvidia RTX 3050 4GB, com Python 3.10 e com versões contidas em: yolov3/requirements.txt

Após treinamento com 50 épocas a rede atingiu um bom resultado na classificação das duas classes, patinho e lilica:
Class	 P (Precision)	R (Recall)	mAP50	   mAP50-95
all	      0.965	         1	      0.995	     0.81
lilica	  0.934	         1	      0.995	     0.842
patinho	  0.996	         1	      0.995	     0.777

Os pesos gerados pelo treinamento estão em: yolo3/runs/train/PatinhoLilica_YOLOv37
Já os resultados do teste estão em: yolo/runs/detect/exp4

A seguir estão algumas imagens do teste:
![Detecção Patinho](https://drive.google.com/file/d/1OicYQpvxOat-STTeB1ay9ZLI28ySAVWA/view)
![Detecção Lilica](https://drive.google.com/file/d/1QaBrRsGtWT5QzzMLip_-Q9_s5PJdy6KP/view)
![Detecção Ambos](https://drive.google.com/file/d/1_D6mH1IiaokXx4BdiQqpx_1urIFG2KKr/view)
