## Students

| **Student** | **Skills**              | **Preferences**          | **Constraints**                    |
|-------------|-------------------------|--------------------------|------------------------------------|
| Alice       | Python, Machine Learning| P1 > P3 > P2 > P4        | Prefers individual project         |
| Bob         | Writing, UX Design      | P3 > P2 > P4 > P1        | None                               |
| Carol       | Java, Research          | P2 > P1 > P3 > P4        | Wants to work with Bob             |
| David       | Python, Web Development | P4 > P1 > P2 > P3        | Available only for P1 or P4        |
| Eve         | Data Analysis, Writing  | P2 > P4 > P1 > P3        | Prefers a group project            |
| Frank       | C++, Systems Design     | P4 > P3 > P1 > P2        | None                               |


## Projects

| **Project** | **Skill Requirements**      | **Capacity** | **Priority** |
|-------------|-----------------------------|--------------|--------------|
| P1          | Python, Machine Learning    | 1-2 students | High         |
| P2          | Java, Data Analysis         | 2-3 students | Medium       |
| P3          | Writing, UX Design          | 1-2 students | Low          |
| P4          | Systems Design, Web Dev     | 1-3 students | High         |


## Constraints:

1. **Project-Specific**:
   - P1: Must include at least one student proficient in Python.
   - P2: Must have at least one student with Java and one with Data Analysis skills.
   - P3: Requires students with Writing or UX Design skills.
   - P4: Requires a mix of technical (C++, Systems Design) and creative (Web Development) skills.

2. **Student-Specific**:
   - Alice prefers working solo and should not be assigned to group projects.
   - Bob and Carol must work on the same project.
   - David can only work on P1 or P4 due to scheduling conflicts.
   - Eve prefers group projects and should not be assigned to individual ones.
        

## Output

| **Student** | **Assigned Project** |
|-------------|----------------------|
| Alice       | P1                   |
| Bob         | P3                   |
| Carol       | P2                   |
| David       | P4                   |
| Eve         | P2                   |
| Frank       | P4                   |

### **Total Preference Score**: 58



