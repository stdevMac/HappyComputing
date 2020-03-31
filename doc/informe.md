# Reporte de Simulación basada en Eventos Discretos

## Marcos Antonio Maceo Reyes `C-412`

### Orden del problema

Happy Computing es un taller de reparaciones electrónicas donde se realizan
las siguientes actividades (el precio de cada servicio se muestra entre paréntesis):
1. Reparación por garantı́a (Gratis)
2. Reparacón fuera de garantá (350pesos)
3. Cambio de equipo (500pesos)
4. Venta de equipos reparados (750pesos)

Se conoce además que el taller cuenta con 3 tipos de empleados: Vendedor,
Técnico y Técnico Especializado.
Para su funcionamiento, cuando un cliente llega al taller, es atendido por un
vendedor y en caso de que el servicio que requiera sea una Reparacón (sea de tipo
1 o 2) el cliente debe ser atendido por un técnico (especializado o no). Además
en caso de que el cliente quiera un cambio de equipo este debe ser atendido por
un técnico especializado. Si todos los empleados que pueden atender al cliente
están ocupados, entonces se establece una cola para sus servicios. Un técnico
especializado sólo realizará Reparaciones si no hay ningún cliente que desee un
cambio de equipo en la cola.
Se conoce que los clientes arriban al local con un intervalo de tiempo que
distribuye Poisson con λ = 20minutos y que el tipo de servicios que requieren
pueden ser descrito mediante la tabla de probabilidades:


| Tipo de servicio | Probabilidad  |
| ---------------- |:-------------:|
| 1                | 0.45          |
| 2                | 0.25          |
| 3                | 0.1           |
| 4                | 0.2           |

Además se conoce que un técnico tarda un tiempo que distribuye exponecial
con λ = 20minutos, en realizar una Reparación cualquiera. Un técnico espe-
cializado tarda un tiempo que distribuye exponencial con λ = 15minutos para
realizar un cambio de equipos y la vendedora puede atender cualquier servicio
en un tiempo que distribuye normal (N(5 min, 2mins)).

El dueño del lugar desea realizar una simulación de la ganancia que tendrı́a en
una jornada laboral si tuviera 2 vendedores, 3 técnicos y 1 técnico especializado.

### Solución

#### Consideraciones

Este problema puede ser modelado a partir de eventos discretos, y así mediante 
simulaciones, se puede determinar un aproximado de la ganancia que se obtendrá.

Se tomo en cuanta que la jornada laboral es de 8 horas y además que dado el 
tiempo que demora en atender un vendedor distribuye normal, y los valores 
pueden ser negativos se toman sus valores modularmente.

####  Modelo

Para realizar el modelo se siguió el principio de analizar minuto a minuto 
los posibles comportamientos de los empleados del taller. Para seguir esa 
idea nos auxiliamos de las siguientes variables:

- variables para el tiempo que resta para que llegue el proximo cliente.
- listas por cada tipo de empleo de acuerdo a la cantidad de trabajadores 
en el cargo, respondiendo a el tiempo que le queda para terminar con el 
cliente que se encuentra atendiendo.
- Cola por cada uno de los empleos mostrando la cantidad de clientes en 
espera por ser atendido.

El flujo de la simulacion consiste en analizar por cada empleo tratar de 
atender la mayor cantidad de clientes y obtener las ganancias. Tras entrar 
un nuevo cliente en el taller este es puesto automaticamente en la cola de 
los vendedores, y de acuerdo a el tipo de servicio que necesiten, será 
puesto el cliente en la cola de los técnicos o los técnicos especializados. 
En el caso de que todos los técnicos se encuentren trabajando y algún 
especialista se encuentre libre, si llega algún cliente este será atendido 
por un especialista.

#### Conclusiones

A partir de las simulaciones del modelo anteriormente planteado se puede 
observar que la ganancia promedio es de 530~590 pesos.
