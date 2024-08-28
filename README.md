# Multi-Robot-Agricultural-feild-Monitoring-(Computer-Vision)

In this project, I investigate a sophisticated multi- robot behavior model for enhancing selective pest control in precision agriculture. This model is particularly relevant for practical applications in farming, where it can significantly improve the ef- ficiency and precision of pest management, reduc- ing the dependency on broad-spectrum pesticides and thereby minimizing environmental impacts.
The methodology integrates a combination of the K-Means clustering algorithm, the Convex Hull algorithm[10], and the A* pathfinding al- gorithm[6]. Initially, the K-Means algorithm is employed to segment a field of dimensions F×F units into kk sectors, each assigned to a robot. The Convex Hull algorithm is then used to define the operational boundaries for each robot, en- suring comprehensive coverage without overlap. Finally, the A* algorithm guides the robots effi- ciently to and within their assigned sectors.
The key attributes of this behavior under study include the effectiveness of sector division, the op- timality of the pathfinding to and within sectors, and the thoroughness of sector coverage. The K- Means algorithm facilitates a logical and balanced division of the field, while the Convex Hull algo- rithm provides clear and precise boundary defini- tions. The A* algorithm, known for its pathfind- ing efficiency, ensures that robots reach their des- ignated sectors and cover them thoroughly for pest detection and control.
To validate this model, I conducted simula- tions focusing on the time efficiency of field cover- age, the completeness of sector scanning, and the pathfinding efficiency. The results demonstrated robust performance in terms of sector coverage and path optimization, with each robot system- atically scanning its assigned sector.
The necessity of this model for selective pest control is underscored by its capability for precise area coverage. This allows for the accurate identi- fication of pest-affected areas, enabling localized treatment interventions and reducing the need for widespread pesticide use. Such a targeted ap- proach conserves beneficial organisms and min- imizes environmental harm, aligning with sus- tainable agricultural practices. The encouraging outcomes from the simulations suggest that this multi-robot system model has great potential for real-world applications in precision agriculture, especially in integrated pest management strategies.





https://github.com/user-attachments/assets/618f70c3-ffca-4edd-900e-bf65ef85f9c3



https://github.com/user-attachments/assets/f6cb9e1c-738b-4bec-bd01-d4dfac54477e




# Mathematical Model

In developing a mathematical model for a multi- robot system designed to scan an agricultural field, we consider various aspects including the robots’ capabilities, the environment, and the al- gorithms used for sector division and navigation. The model is based on a hypothetical scenario of a 20x20 unit agricultural field which is to be scanned by a fleet of five robots.

![Picture2](https://github.com/user-attachments/assets/496b0b9b-fca6-483d-96bb-1e1bccaeb216)

The field is assumed to be a flat, two- dimensional, bounded area without any internal obstacles, simplifying the modeling and algorithm design. For effective planning and tracking of the robots’ movements, the field is discretized into a 10x10 grid, where each grid cell represents a 2x2 unit area. This grid structure aids in defin- ing the operational space for the robots and in implementing navigation algorithms.
Each robot in the fleet is equipped with a sens- ing diameter of 2 units, allowing it to scan an area within a radius of 1 unit around its current location. Additionally, the robots have a com- munication range of 3 units, enabling them to communicate with other robots within this range. This setup is crucial for coordinated movement and scanning, as well as for avoiding overlapping areas during the scanning process.
The robots are considered autonomous, ca- pable of independent movement and decision- making, but they can also communicate with oth- ers within their communication range. The po- sitions of the robots are defined by coordinates (x, y) in the field. For the purpose of sector di-
vision, the field is divided into five sectors us- ing the K-Means clustering algorithm. This al- gorithm determines the centroids of the sectors, denoted as Ci=(xi,yi), where ii ranges from 1 to 5, representing each sector. The K-Means algo- rithm aims to minimize the within-cluster sum of squares (WCSS), which is defined as:


$$
\text{WCSS} = \sum_{j=1}^{k} \sum_{p_i \in S_j} ||p_i - c_j||^2 \quad (1)
$$


## Sector Division and Convex Hull Determination

After dividing the field into sectors using the K-Means algorithm, the boundary of each sector is determined using the convex hull algorithm. The convex hull of a set of points in a plane is the smallest convex polygon that contains all the points. This step is crucial as it defines the operational area for each robot, ensuring that they operate within their assigned sectors and do not overlap with others. The Graham Scan algorithm computes the convex hull for a given set of points in the plane.

### Steps to Compute the Convex Hull using Graham Scan

1. **Select the starting point**:
   - Choose the point \( p_0 \) with the lowest y-coordinate (or the lowest x-coordinate in case of ties).
   - Let \( p_0 = (x_0, y_0) \).

2. **Sort the points**:
   - Sort the remaining points based on the polar angle they make with \( p_0 \) in counterclockwise order.
   - The angle \( \theta_i \) for point \( p_i = (x_i, y_i) \) is calculated as \( \theta_i = \text{atan2}(y_i − y_0, x_i − x_0) \).

3. **Initialize the stack**:
   - Start with a stack and push \( p_0 \), \( p_1 \), and \( p_2 \) onto it.

4. **Process the points**:
   - For each point \( p_i \) (starting from \( i = 3 \)):
     1. While the stack has at least two points and the sequence of the second-to-top, top, and \( p_i \) makes a non-left turn (determined by the cross product), pop the top point off the stack.
     2. Push \( p_i \) onto the stack.

5. **Result**:
   - The points remaining on the stack represent the vertices of the convex hull in counterclockwise order.

### Non-Left Turn Check

The non-left turn check is performed by calculating the cross product of vectors \( \vec{AB} \) and \( \vec{BC} \), where \( A \), \( B \), and \( C \) are consecutive points with \( B \) and \( C \) on top of the stack. The cross product is given by:

$$
(b_x − a_x)(c_y − b_y) − (b_y − a_y)(c_x − b_x)
$$

A non-positive value indicates a non-left turn.

## Robot Sector Assignment and Navigation

Once the sectors are defined, each robot is assigned to the nearest sector based on the Euclidean distance to the sector centroids. The robots then navigate their assigned sectors using the A* algorithm. The choice of A* is due to its efficiency and optimality in grid-based environments, making it suitable for navigating the discretized field. The robots’ paths are designed to ensure complete coverage of their assigned sectors.

### Scanning Process

After reaching their assigned sectors, the robots begin the scanning process:

1. **Movement**:
   - The robots move from grid to grid within the sector. This systematic grid-by-grid movement ensures complete coverage of the sector.

2. **Scanning**:
   - At each grid point, the robots scan the area within their sensing range (a circle with a radius of 1 unit).
   - This methodical approach guarantees that no areas are missed and that the entire sector is thoroughly scanned.
## Theoretical Analysis

### K-Means Clustering for Sector Division

Given a field of dimensions \( L \times W \) and a set of \( N \) points representing locations in the field \( P = \{p_1, p_2, \dots, p_N \} \), where each \( p_i \) is a coordinate \( (x_i, y_i) \), and a number of robots (and hence sectors) \( k \), we aim to partition \( P \) into \( k \) clusters (sectors) each represented by a centroid \( C = \{c_1, c_2, \dots, c_k \} \).

1. **Initialization**: 
   - Select \( k \) initial centroids randomly from \( P \).

2. **Assignment Step**:
   - Each point \( p_i \) is assigned to the nearest centroid, forming \( k \) clusters. Mathematically, \( p_i \) is assigned to cluster \( j \) if:
     $$
     j = \arg\min_{j} ||p_i − c_j|| \quad (2)
     $$
   - where \( ||p_i − c_j|| \) is the Euclidean distance between \( p_i \) and \( c_j \).

3. **Update Step**:
   - Recompute each centroid \( c_j \) as the mean of all points assigned to it:
     $$
     c_j = \frac{1}{|S_j|} \sum_{p_i \in S_j} p_i \quad (3)
     $$
   - where \( S_j \) is the set of points in cluster \( j \).

4. **Convergence**:
   - The process repeats until centroids \( c_j \) no longer change significantly.

### A* Algorithm

To mathematically prove that a robot, given any starting position, can reach a corner of its assigned sector using the A* algorithm, we need to establish the properties of the A* algorithm and the nature of the environment in which the robot operates.

#### Assumptions

1. The field is represented as a graph where each point (or grid cell) in the sector is a node, and adjacent points are connected by edges.
2. The robot’s starting position is denoted as node \( s \) in the graph.
3. The target corner position is denoted as node \( t \).
4. The cost to move from one node to an adjacent node is uniform and denoted as \( c \).

#### A* Algorithm's Cost Function

The A* algorithm finds the shortest path from node \( s \) to node \( t \) using the cost function:
$$
f(n) = g(n) + h(n)
$$
where \( g(n) \) is the actual cost from \( s \) to \( n \), and \( h(n) \) is the heuristic estimated cost from \( n \) to \( t \).

#### Heuristic Function

The heuristic function \( h(n) \) is admissible and is often chosen as the Euclidean or Manhattan distance:
$$
h(n) = d(n, t)
$$
where \( d(n, t) \) is the distance from \( n \) to \( t \).

#### Proof of Reachability

1. There exists at least one path from \( s \) to \( t \) in a connected graph.
2. A* finds the shortest path due to the admissibility of \( h(n) \).
3. For each node \( n \), \( g(n) \) is the cost of the cheapest path from \( s \) to \( n \). A* expands nodes in order of increasing \( f(n) \).
4. A* will eventually expand node \( t \) as the number of nodes is finite.
5. If \( h(n) \) is consistent, A* finds the shortest path without reprocessing any node.

#### Conclusion

Given the connected nature of the graph representing the sector and the properties of the A* algorithm, it is mathematically proven that the robot can always reach the corner of its assigned sector from any starting position.



This project successfully demonstrated the viability of a multi-robot system in precision agriculture, focusing on sector division, boundary determination, and efficient pathfinding. The implementation utilized a combination of K-Means clustering, Convex Hull, and A* algorithms. The results are presented in three main areas:

1. **Sector Division and Boundary Determination**
2. **Pathfinding Efficiency**
3. **Overall System Performance in a Simulated Agricultural Environment**

### Sector Division and Boundary Determination

The K-Means algorithm effectively divided a simulated field into specified sectors. For a field of dimensions 20×20 units and 5 robots, the algorithm efficiently partitioned the area, ensuring a balanced distribution of workload among the robots.

The subsequent application of the Convex Hull algorithm provided clear and precise boundaries for each sector. This was evidenced by the non-overlapping convex polygons formed around each cluster of points, ensuring that each robot had a distinct operational area.

![Picture3](https://github.com/user-attachments/assets/5db58f01-c029-450b-ac51-cc6180ef1e43)

*Figure 2: Red dots are the robots, X1, X2, ..., Xn are the sectors.*

In Figure 2, the boundaries of each sector in the 20x20 field are illustrated. The sectors are assigned to the robots based on their proximity to the sector centroids. The assignments are as follows:

- **Robot 2** is assigned to **Sector 1**.
- **Robot 3** is assigned to **Sector 4**.
- **Robot 1** is assigned to **Sector 3**.
- **Robot 5** is assigned to **Sector 5**.
- **Robot 4** is assigned to **Sector 2**.

Each robot’s position is marked with a red dot, labeled with its corresponding number. The sectors are outlined with black lines, showing the convex hull of the points in each sector. The centroids of the sectors are marked with black X symbols, each labeled with the sector number. This visualization provides a clear view of the sector boundaries and the respective robots assigned to each sector, ensuring efficient coverage of the field from their initial random positions.

### Pathfinding Efficiency

The implementation of the A* algorithm demonstrated optimal pathfinding from any given starting position within a sector to predetermined target points, typically the corners of the sector. The algorithm consistently found the shortest path, taking into account the costs associated with traversing different nodes. The heuristic function, based on either Euclidean or Manhattan distance, proved to be effective and admissible, contributing to the algorithm’s efficiency.

![picture4](https://github.com/user-attachments/assets/a7ff6ff0-429e-4a8e-9ffa-3abe8040598d)

*Figure 3: Robot moving to the corner of the assigned sector.*

### System Performance in Simulation

In a simulated agricultural environment, the multi-robot system showed remarkable efficiency. The robots, each operating in their assigned sectors, covered the entire field systematically. The division of labor prevented redundancy and overlapping, enhancing the overall scanning process’s efficiency.



https://github.com/user-attachments/assets/93857af9-7ce5-4fc9-8aeb-e2c0645077bb


*Figure 4: Robot scanning the assigned sector of the agricultural field.*

The simulation results presented in Figure 4 demonstrate the coverage achieved by the robots. Each robot’s assigned sector is represented by an irregular pentagon-shaped area, and the scanning coverage within this sector is highlighted in green. The robots themselves are depicted as smaller circles, with their sensing ranges indicated by larger concentric circles.

## Conclusion

The results from this project underscore the potential of using a multi-robot system for precision agriculture. The combination of K-Means clustering for sector division, Convex Hull for boundary determination, and A* for efficient pathfinding showed that such systems could significantly enhance operational efficiency in agricultural settings. These findings pave the way for further research and real-world application of multi-robot systems in agriculture, particularly for tasks requiring precise and efficient area coverage, such as selective pest control.


