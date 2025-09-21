Detecção e Classificação de Imagens com Deep Learning
Este projeto utiliza uma rede neural de Deep Learning para detectar e classificar duas classes de objetos: um patinho de pelúcia e uma preguiça de pelúcia ("Lilica").

Dataset
O dataset foi construído a partir de 89 imagens originais, que foram processadas e divididas em três conjuntos:

Treino: 50 imagens originais, com um acréscimo de 100 imagens criadas via Data Augmentation (Cisalhamento, Rotação e Inversão).

Localização: yolov3/dataset/train

Validação: 25 imagens.

Localização: yolov3/dataset/valid

Teste: 25 imagens.

Localização: yolov3/dataset/test

Arquitetura e Ambiente
A rede neural utilizada foi a YOLOv3, implementada com o framework PyTorch.

Hardware: GPU NVIDIA GeForce RTX 3050 4GB

Linguagem: Python 3.10

Dependências: As versões das bibliotecas estão detalhadas no arquivo yolov3/requirements.txt.

Resultados
Após um treinamento de 50 épocas, a rede alcançou excelentes resultados na validação, demonstrando alta precisão e recall para ambas as classes.

Classe	Precision (P)	Recall (R)	mAP@.50	mAP@.50-.95
all	0.965	1.000	0.995	0.810
lilica	0.934	1.000	0.995	0.842
patinho	0.996	1.000	0.995	0.777

Exportar para as Planilhas
Os pesos gerados pelo treinamento estão em: yolov3/runs/train/PatinhoLilica_YOLOv37/

As imagens de resultado da fase de teste estão em: yolov3/runs/detect/exp4/

Exemplos de Detecção
A seguir, alguns exemplos de inferência do modelo em imagens do conjunto de teste.

Detecção do Patinho
Detecção da Lilica
Detecção de Ambos
