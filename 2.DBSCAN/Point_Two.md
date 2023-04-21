## b.What are the mathematical fundamentals of it?


El método de clustering DBSCAN (Density-Based Spatial Clustering of Applications with Noise) es un algoritmo de aprendizaje no supervisado utilizado para agrupar puntos de datos en clusters. Este método se basa en la densidad de los puntos y no requiere que el número de clusters sea especificado previamente.

#### Los fundamentos matemáticos del método DBSCAN incluyen:

Definición de un radio de búsqueda: se define un radio de búsqueda para cada punto de datos en el espacio. Este radio se utiliza para determinar los puntos cercanos a cada punto de datos.
Definición de un umbral de densidad: se define un umbral de densidad, que se utiliza para determinar si un punto de datos es un punto central o un punto de borde. Este umbral se utiliza para determinar si un punto de datos tiene suficientes puntos cercanos dentro del radio de búsqueda para ser considerado un punto central.
Identificación de puntos centrales y puntos de borde: se identifican los puntos centrales y los puntos de borde en función del umbral de densidad y del número de puntos cercanos dentro del radio de búsqueda.
Formación de clusters: los puntos centrales y los puntos de borde se utilizan para formar los clusters. Los puntos centrales se agrupan en clusters y los puntos de borde se asignan a los clusters correspondientes si están dentro del radio de búsqueda de un punto central.
Identificación de ruido: los puntos que no son puntos centrales ni puntos de borde se consideran ruido y no se asignan a ningún cluster.

En resumen, el método DBSCAN utiliza la densidad de los puntos de datos para identificar clusters en el espacio. Los puntos cercanos dentro de un radio de búsqueda se utilizan para definir la densidad de un punto de datos y para identificar los puntos centrales y los puntos de borde. Estos puntos se utilizan para formar los clusters y los puntos que no se asignan a ningún cluster se consideran ruido.