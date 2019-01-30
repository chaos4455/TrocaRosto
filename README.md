# Troca rosto - Face swap

Objetivo:

- Realizar a identificação e troca de rosto em imagens através de duas imagens, uma origem, outra de destino.

- Acha que pode acrescentar algo interessante, fazer alguma melhoria ou correção? Fique a vontade!

- Como rodar a aplicação? ﻿Execute o comando faceswap.py origem.jpg destino.jpg e isso vai gerar uma imagem chamada resultado.jpg

- Devo fazer mais alguma coisa? Sim! Mude o arquivo "shape_predictor_68_face_landmarks.dat" para o caminho "C:\shape_predictor_68_face_landmarks.dat\shape_predictor_68_face_landmarks.dat"

- Abra o arquivo "/core/recognizer.py " e altere as linha de 63 a 67 com os dados obtidos no site: faceplusplus.com conforme a instrução.

```python
def landmarks_by_face__(image):
    url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
    params = {
        'api_key': 'sua chave aqui',
        'api_secret': 'seu segredo aqui',
```        

# Exemplos e resultados:


- Barack Obama
![](https://github.com/chaos4455/TrocaRosto/blob/master/Exemplos/Barack%20Obama.jpg?raw=true)

- Ronaldinho Gaúcho
![](https://github.com/chaos4455/TrocaRosto/blob/master/Exemplos/Ronaldinho%20Ra%C3%BAcho.jpg?raw=true)

- Ronaldo Obama ou Obama Gaúcho
![](https://github.com/chaos4455/TrocaRosto/blob/master/Exemplos/Ronaldo%20Obama.jpg?raw=true)



- Updates:

30/01/2019 05:22
Feito upload inicial do projeto. 

