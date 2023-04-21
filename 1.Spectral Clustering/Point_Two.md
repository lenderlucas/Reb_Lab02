## b. What are the mathematical fundamentals of it?

El método de agrupamiento espectral (Spectral Clustering) utiliza técnicas de álgebra lineal y teoría de grafos para clasificar los datos en diferentes grupos (clusters) en función de sus similitudes. A continuación se describen los fundamentos matemáticos del método de clustering espectral:

### Matriz de similitud: 
La primera etapa del método de clustering espectral es calcular una matriz de similitud que refleje las similitudes entre todas las parejas de datos. Esta matriz puede ser calculada utilizando diferentes medidas de similitud, como la distancia euclidiana o el coeficiente de correlación. Una vez que se ha calculado la matriz de similitud, se puede pensar en ella como una representación gráfica de los datos, donde cada punto de datos se representa como un nodo en el grafo y la similitud entre los puntos se representa como los pesos de las aristas entre los nodos.

### Grafo: 
A partir de la matriz de similitud, se construye un grafo no dirigido, donde cada punto de datos se representa como un nodo y la similitud entre los puntos se representa como los pesos de las aristas entre los nodos. El grafo puede ser construido utilizando diferentes criterios, como un grafo completo (cada nodo está conectado con todos los demás nodos) o un grafo de vecinos cercanos (cada nodo está conectado con sus vecinos más cercanos).

### Descomposición espectral: 
Después de construir el grafo, se calcula la descomposición espectral de la matriz de Laplaciano del grafo. El Laplaciano del grafo es una matriz que se puede calcular a partir de la matriz de adyacencia del grafo y que refleja la conectividad y la estructura del grafo. La descomposición espectral de la matriz de Laplaciano produce un conjunto de vectores propios y valores propios que se utilizan para clasificar los datos en diferentes grupos.

## Clustering: 
Se aplica un algoritmo de clustering, como k-means, a los vectores propios calculados en la descomposición espectral para clasificar los datos en diferentes grupos. Los vectores propios correspondientes a los valores propios más pequeños suelen ser los más informativos para el clustering, ya que reflejan las estructuras de cluster más significativas del grafo.

En resumen, el método de clustering espectral utiliza técnicas de álgebra lineal y teoría de grafos para calcular una matriz de similitud, construir un grafo a partir de la matriz de similitud, calcular la descomposición espectral del Laplaciano del grafo y aplicar un algoritmo de clustering a los vectores propios calculados para clasificar los datos en diferentes grupos.