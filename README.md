# Multi-Robot-Agricultural-feild-Monitoring-(Computer-Vision)

In this project, I investigate a sophisticated multi- robot behavior model for enhancing selective pest control in precision agriculture. This model is particularly relevant for practical applications in farming, where it can significantly improve the ef- ficiency and precision of pest management, reduc- ing the dependency on broad-spectrum pesticides and thereby minimizing environmental impacts.
The methodology integrates a combination of the K-Means clustering algorithm, the Convex Hull algorithm[10], and the A* pathfinding al- gorithm[6]. Initially, the K-Means algorithm is employed to segment a field of dimensions F×F units into kk sectors, each assigned to a robot. The Convex Hull algorithm is then used to define the operational boundaries for each robot, en- suring comprehensive coverage without overlap. Finally, the A* algorithm guides the robots effi- ciently to and within their assigned sectors.
The key attributes of this behavior under study include the effectiveness of sector division, the op- timality of the pathfinding to and within sectors, and the thoroughness of sector coverage. The K- Means algorithm facilitates a logical and balanced division of the field, while the Convex Hull algo- rithm provides clear and precise boundary defini- tions. The A* algorithm, known for its pathfind- ing efficiency, ensures that robots reach their des- ignated sectors and cover them thoroughly for pest detection and control.
To validate this model, I conducted simula- tions focusing on the time efficiency of field cover- age, the completeness of sector scanning, and the pathfinding efficiency. The results demonstrated robust performance in terms of sector coverage and path optimization, with each robot system- atically scanning its assigned sector.
The necessity of this model for selective pest control is underscored by its capability for precise area coverage. This allows for the accurate identi- fication of pest-affected areas, enabling localized treatment interventions and reducing the need for widespread pesticide use. Such a targeted ap- proach conserves beneficial organisms and min- imizes environmental harm, aligning with sus- tainable agricultural practices. The encouraging outcomes from the simulations suggest that this multi-robot system model has great potential for real-world applications in precision agriculture, especially in integrated pest management strategies.


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


