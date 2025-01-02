# Set of students
set STUDENTS;

# Set of projects
set PROJECTS;

# Set of skills
set SKILLS;

# Preference score of student i for project j
param preference {STUDENTS, PROJECTS};

# Minimum capacity for each project
param min_cap {PROJECTS};

# Maximum capacity for each project
param max_cap {PROJECTS};

# 1 if student i has skill k, 0 otherwise
param student_skills {STUDENTS, SKILLS};

# 1 if project j requires skill k, 0 otherwise
param project_requirements {PROJECTS, SKILLS};

# 1 if student prefers individual projects
param individual {STUDENTS} default 0;

# 1 if student i can be assigned to project j
param available {STUDENTS, PROJECTS} default 1;

# Students who must work together
set must_work_together within STUDENTS cross STUDENTS;

# Decision Variables: 1 if student i is assigned to project j
var x {STUDENTS, PROJECTS} binary;

# Objective: Maximize total preference score
maximize TotalPreference:
    sum {i in STUDENTS, j in PROJECTS} preference[i, j] * x[i, j];

# Each student can be assigned to at most one project
subject to AssignOnce {i in STUDENTS}:
    sum {j in PROJECTS} x[i, j] <= 1;

# Respect project capacities
subject to ProjectMinCap {j in PROJECTS}:
    sum {i in STUDENTS} x[i, j] >= min_cap[j];

subject to ProjectMaxCap {j in PROJECTS}:
    sum {i in STUDENTS} x[i, j] <= max_cap[j];

# Skill requirements for each project
subject to SkillMatch {j in PROJECTS, k in SKILLS: project_requirements[j, k] = 1}:
    sum {i in STUDENTS: student_skills[i, k] = 1} x[i, j] >= 1;

# Individual project preference
subject to IndividualPref {i in STUDENTS, j in PROJECTS: individual[i] = 1 and min_cap[j] > 1}:
    x[i, j] = 0;

# Availability constraints
subject to Availability {i in STUDENTS, j in PROJECTS: available[i, j] = 0}:
    x[i, j] = 0;


# Students who must work together
subject to Pairing {(s1, s2) in must_work_together, p in PROJECTS}:
    x[s1, p] = x[s2, p];
