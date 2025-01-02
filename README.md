# Student Project Pairing Problem

The **Student Project Pairing Problem** involves assigning students to projects in a way that maximizes overall satisfaction, respects skill requirements, adheres to project capacities, and satisfies specific constraints. It is a combinatorial optimization problem commonly encountered in educational settings or team-based project environments.

## Problem Description

### Objective
The goal is to assign students to projects such that:
- The total preference score across all student-project assignments is maximized.
- All constraints (e.g., capacity, skill requirements, availability) are satisfied.

### Input Data

1. A set of **students**, each characterized by:
   - **Skills**: The abilities or knowledge areas a student possesses (e.g., Python, UX Design).
   - **Preferences**: A ranked or scored list of preferred projects (higher scores indicate higher preference).
   - **Constraints**: Special conditions, such as:
      - **Availability**: A student can only work on specific projects.
      - **Group preference**: A student prefers individual or group projects.
      - **Pairing**: A student must (or must not) work with specific peers.

2. A set of **projects**, each characterized by:
   - **Skill Requirements**: A list of required skills that must be covered by the assigned students.
   - **Capacity**: Minimum and maximum number of students allowed to work on the project.
   - **Priority**: Some projects may have higher priority and need special consideration.

3. Each student-project pair has a **preference score**, representing how much a student would like to work on a particular project. These scores are used to guide the optimization process.


### Constraints

1. **Assignment Constraint**: Each student can be assigned to at most one project.

2. **Capacity Constraints**: Each project must have a number of assigned students between its minimum and maximum capacity.

3. **Skill Matching**: The assigned students must collectively cover all the required skills for each project.

4. **Student-Specific Constraints**:
   - **Individual Projects**: Some students prefer working alone.
   - **Pairing**: Certain students must (or must not) work together.
   - **Availability**: Students may only be available for specific projects.

5. **Project-Specific Constraints**: Some projects may require diverse teams, such as a mix of technical and creative skills.




## Mathematical Formulation

### Decision Variables
Let $x_{ij}$ be a binary variable:
- $x_{ij} = 1$ if student $i$ is assigned to project $j$.
- $x_{ij} = 0$ otherwise.


### Parameters
1. **Student preferences**: $P_{ij}$​ is the preference score of student $i$ for project $j$. Higher scores represent more preferred projects.
2. **Project capacities**:
   - $\text{min\\_cap}_j$: minimum number of students required for project $j$.
   - $\text{max\\_cap}_j$: maximum number of students allowed for project $j$.
3. **Skills**:
   - $S_{ik}=1$ if student $i$ has skill $k$, otherwise $S_{ik}=0$.
   - $R_{jk}=1$ if project $j$ requires skill $k$, otherwise $R_{jk}=0$.

### Objective Function
Maximize the total preference score:
```math
\text{Maximize } \sum_{i \in \text{Students}} \sum_{j \in \text{Projects}} P_{ij} x_{ij}
```

### Constraints
1. **Assignment constraint.** Each student can be assigned to at most one project: 
```math
\sum_{j \in \text{Projects}} x_{ij} \leq 1 \quad \forall i \in \text{Students}
```

2. **Capacity constraints.** Each project must have a number of assigned students within its capacity:
```math
\text{min\_cap}_j \leq \sum_{i \in \text{Students}} x_{ij} \leq \text{max\_cap}_j \quad \forall j \in \text{Projects}
```

3. **Skill Matching.** For each project $j$, the required skills $R_{jk}$​ must be covered by at least one assigned student:
```math
\sum_{i \in \text{Students}} S_{ik} x_{ij} \geq R_{jk} \quad \forall j \in \text{Projects}, \forall k \in \text{Skills}
```

4. **Individual project preference constraints.** Students who prefer individual projects can only be assigned to single-capacity projects:
```math
x_{ij} = 0 \quad \forall i \in \text{Students (preferring individual)}, \forall j \in \text{Group Projects}
```

5. **Pairing constraints.** If students $i_1$​ and $i_2$​ must work together, they should be assigned to the same project:
```math
x_{i_1 j} = x_{i_2 j} \quad \forall j \in \text{Projects}, \text{ if } i_1 \text{ and } i_2 \text{ must work together.}
```

6. **Availability constraints.** If a student $i$ is only available for certain projects $j$, enforce:
```math
x_{ij} = 0 \quad \forall j \notin \text{Available Projects for } i
```


## Example

| **Student** | **Skills**              | **Preferences**          | **Constraints**                   |
|-------------|-------------------------|--------------------------|------------------------------------|
| Alice       | Python, Machine Learning| P1 > P3 > P2 > P4        | Prefers individual project         |
| Bob         | Writing, UX Design      | P3 > P2 > P4 > P1        | None                               |
| Carol       | Java, Research          | P2 > P1 > P3 > P4        | Wants to work with Bob             |
| David       | Python, Web Development | P4 > P1 > P2 > P3        | Available only for P1 or P4        |
| Eve         | Data Analysis, Writing  | P2 > P4 > P1 > P3        | Prefers a group project            |
| Frank       | C++, Systems Design     | P4 > P3 > P1 > P2        | None                               |


| **Project** | **Skill Requirements**      | **Capacity** | **Priority** |
|-------------|-----------------------------|--------------|--------------|
| P1          | Python, Machine Learning    | 1-2 students | High         |
| P2          | Java, Data Analysis         | 2-3 students | Medium       |
| P3          | Writing, UX Design          | 2 students   | Low          |
| P4          | Systems Design, Web Dev     | 1-3 students | High         |


#### Output

| **Student** | **Assigned Project** |
|-------------|----------------------|
| Alice       | P1                   |
| Bob         | P3                   |
| Carol       | P3                   |
| David       | P4                   |
| Eve         | P2                   |
| Frank       | P4                   |

#### **Total Preference Score**: 48


---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

