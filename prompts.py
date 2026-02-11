import random
COMPUTER_SCIENCE_DOMAINS = {
    "Algorithms and Data Structures": [
        "Algorithm Analysis",
        "Sorting and Searching",
        "Graph Algorithms",
        "Dynamic Programming",
        "Greedy Algorithms",
        "Divide and Conquer",
        "Linear Data Structures",
        "Tree Data Structures",
        "Hash Tables",
        "Heaps and Priority Queues",
        "Advanced Data Structures"
    ],
    "Theory of Computation": [
        "Computational Complexity",
        "Formal Languages",
        "Automata Theory",
        "Computability Theory",
        "Logic and Proof Systems",
        "Cryptographic Theory",
        "Information Theory",
        "Quantum Computing Theory"
    ],
    "Programming Languages": [
        "Programming Language Design",
        "Compilers and Interpreters",
        "Type Systems",
        "Functional Programming",
        "Object-Oriented Programming",
        "Concurrent Programming",
        "Domain-Specific Languages",
        "Programming Language Semantics",
        "Code Optimization",
        "API Integration",
        "Scripting Languages"
    ],
    "Computer Systems": [
        "Computer Architecture",
        "Processor Design",
        "Memory Systems",
        "Input/Output Systems",
        "Embedded Systems",
        "Real-Time Systems",
        "Parallel Computing",
        "Distributed Systems",
        "Cloud Computing"
    ],
    "Operating Systems": [
        "Process Management",
        "Memory Management",
        "File Systems",
        "Device Drivers",
        "System Calls",
        "Virtualization",
        "Container Technologies",
        "System Performance",
        "System Security"
    ],
    "Networks and Communications": [
        "Network Protocols",
        "Network Architecture",
        "Wireless Networks",
        "Network Security",
        "Network Performance",
        "Internet Technologies",
        "Mobile Computing",
        "IoT and Sensor Networks",
        "Network Programming"
    ],
    
    "Databases": [
        "Database Design",
        "Relational Databases",
        "NoSQL Databases",
        "Database Management Systems",
        "Query Processing",
        "Database Optimization",
        "Distributed Databases",
        "Data Warehousing",
        "Big Data Systems",
        "Database Security"
    ],
    "Artificial Intelligence": [
        "Knowledge Representation",
        "Expert Systems",
        "Planning and Reasoning",
        "Search Algorithms",
        "Constraint Satisfaction",
        "Multi-Agent Systems",
        "Fuzzy Logic",
        "Symbolic AI",
        "AI Ethics"
        #
        "Image Recognition",
        "Object Detection",
        "Face Recognition",
        "Medical Imaging",
        "Video Analysis",
        "Pattern Recognition",
        "Image Segmentation",
        "Feature Extraction",
        "3D Vision",
        #
        "Image Recognition",
        "Object Detection",
        "Face Recognition",
        "Medical Imaging",
        "Video Analysis",
        "Pattern Recognition",
        "Image Segmentation",
        "Feature Extraction",
        "3D Vision"
    ],
    "Machine Learning": [
        "Supervised Learning",
        "Unsupervised Learning",
        "Reinforcement Learning",
        "Deep Learning",
        "Neural Networks",
        "Statistical Learning",
        "Feature Engineering",
        "Model Evaluation",
        "MLOps",
        "AutoML"
    ],
    
    "Data Science and Analytics": [
        "Data Mining",
        "Statistical Analysis",
        "Data Visualization",
        "Predictive Analytics",
        "Business Intelligence",
        "Data Preprocessing",
        "Exploratory Data Analysis",
        "Time Series Analysis",
        "A/B Testing"
    ],
    
    "Computer Graphics": [
        "2D Graphics",
        "3D Graphics",
        "Rendering Techniques",
        "Computer Animation",
        "Image Processing",
        "Computational Geometry",
        "Virtual Reality",
        "Augmented Reality",
        "Game Graphics"
    ],
    
    # "Computer Vision": [
    #     "Image Recognition",
    #     "Object Detection",
    #     "Face Recognition",
    #     "Medical Imaging",
    #     "Video Analysis",
    #     "Pattern Recognition",
    #     "Image Segmentation",
    #     "Feature Extraction",
    #     "3D Vision"
    # ],
    
    # "Natural Language Processing": [
    #     "Text Processing",
    #     "Language Models",
    #     "Machine Translation",
    #     "Speech Recognition",
    #     "Sentiment Analysis",
    #     "Information Extraction",
    #     "Question Answering",
    #     "Text Generation",
    #     "Computational Linguistics"
    # ],
    # "Robotics": [
    #     "Robot Kinematics",
    #     "Robot Dynamics",
    #     "Path Planning",
    #     "Robot Control",
    #     "Computer Vision for Robotics",
    #     "Human-Robot Interaction",
    #     "Autonomous Systems",
    #     "Robot Learning",
    #     "Swarm Robotics"
    # ],
    "Human-Computer Interaction": [
        "User Interface Design",
        "User Experience Design",
        "Usability Engineering",
        "Accessibility",
        "Information Visualization",
        "Interactive Systems",
        "Cognitive Science",
        "Social Computing",
        "Mobile Interfaces"
    ],
    
    "Software Engineering": [
        "Software Development Methodologies",
        "Requirements Engineering",
        "Software Architecture",
        "Software Testing",
        "Software Maintenance",
        "Version Control",
        "DevOps",
        "Agile Development",
        "Software Quality Assurance",
        "Project Management",
        "Debugging and Testing",
        "Software Requirements",
        "Application Development",
        "System Integration",
        "Licensing and Compliance"
    ],
    "Cybersecurity": [
        "Cryptography",
        "Network Security",
        "Information Security",
        "Application Security",
        "System Security",
        "Digital Forensics",
        "Ethical Hacking",
        "Security Protocols",
        "Privacy Protection",
        "Risk Management"
    ],
    "Web Technologies": [
        "Web Development",
        "Frontend Technologies",
        "Backend Technologies",
        "Web Services",
        "API Design",
        "Web Security",
        "Web Performance",
        "Progressive Web Apps",
        "Web Standards"
    ],
    
    "Mobile Computing": [
        "Mobile App Development",
        "Cross-Platform Development",
        "Mobile UI/UX",
        "Mobile Security",
        "Location-Based Services",
        "Mobile Networks",
        "Wearable Computing",
        "Mobile Game Development"
    ],
    "Game Development": [
        "Game Design",
        "Game Engines",
        "Game Physics",
        "Game AI",
        "Game Graphics",
        "Game Audio",
        "Multiplayer Systems",
        "Game Testing",
        "Virtual Worlds"
    ],
    "Computational Science": [
        "Scientific Computing",
        "Numerical Methods",
        "Simulation and Modeling",
        "High-Performance Computing",
        "Computational Physics",
        "Computational Chemistry",
        "Computational Biology",
        "Mathematical Software"
    ],
    "Bioinformatics": [
        "Sequence Analysis",
        "Structural Bioinformatics",
        "Genomics",
        "Proteomics",
        "Systems Biology",
        "Phylogenetics",
        "Biomedical Informatics",
        "Computational Drug Discovery"
    ],
    "Information Systems": [
        "Management Information Systems",
        "Enterprise Systems",
        "Business Process Management",
        "E-Commerce Systems",
        "Decision Support Systems",
        "Knowledge Management",
        "Information Architecture",
        "Digital Transformation"
    ],
    "Emerging Technologies": [
        "Blockchain Technology",
        "Internet of Things",
        "Edge Computing",
        "Quantum Computing",
        "Augmented Reality",
        "Virtual Reality",
        "5G Technologies",
        "Serverless Computing",
        "Neuromorphic Computing",
        "Robot Kinematics",
        "Robot Dynamics",
        "Path Planning",
        "Robot Control",
        "Computer Vision for Robotics",
        "Human-Robot Interaction",
        "Autonomous Systems",
        "Robot Learning",
        "Swarm Robotics"
    ]
}

def reverse_dict(original_dict):
    """
    反转字典的键值对。如果有重复的值，后面的键会覆盖前面的键。
    
    Args:
        original_dict (dict): 原始字典
    
    Returns:
        dict: 反转后的字典
    """
    reversed_dict = {}
    for key, values in original_dict.items():
        for value in values:
            reversed_dict[value] = key
    return reversed_dict


COMPUTER_SCIENCE_DOMAINS_REVERSED = reverse_dict(COMPUTER_SCIENCE_DOMAINS)
Domain_Classification_Prompt = '''
You are an expert computer science domain classifier. Your task is to analyze questions and classify them into the appropriate computer science domain(s) based on their content, technical focus, and context.

## Algorithms and Data Structures
    - Algorithm Analysis
    - Sorting and Searching
    - Graph Algorithms
    - Dynamic Programming
    - Greedy Algorithms
    - Divide and Conquer
    - Linear Data Structures
    - Tree Data Structures
    - Hash Tables
    - Heaps and Priority Queues
    - Advanced Data Structures

## Theory of Computation
    - Computational Complexity
    - Formal Languages
    - Automata Theory
    - Computability Theory
    - Logic and Proof Systems
    - Cryptographic Theory
    - Information Theory
    - Quantum Computing Theory

## Programming Languages
    - Programming Language Design
    - Compilers and Interpreters
    - Type Systems
    - Functional Programming
    - Object-Oriented Programming
    - Concurrent Programming
    - Domain-Specific Languages
    - Programming Language Semantics
    - Code Optimization

## Computer Systems
    - Computer Architecture
    - Processor Design
    - Memory Systems
    - Input/Output Systems
    - Embedded Systems
    - Real-Time Systems
    - Parallel Computing
    - Distributed Systems
    - Cloud Computing

## Operating Systems
    - Process Management
    - Memory Management
    - File Systems
    - Device Drivers
    - System Calls
    - Virtualization
    - Container Technologies
    - System Performance
    - System Security

## Networks and Communications
    - Network Protocols
    - Network Architecture
    - Wireless Networks
    - Network Security
    - Network Performance
    - Internet Technologies
    - Mobile Computing
    - IoT and Sensor Networks
    - Network Programming

## Databases
    - Database Design
    - Relational Databases
    - NoSQL Databases
    - Database Management Systems
    - Query Processing
    - Database Optimization
    - Distributed Databases
    - Data Warehousing
    - Robotics
    - Database Security

## Artificial Intelligence
    - Knowledge Representation
    - Expert Systems
    - Planning and Reasoning
    - Search Algorithms
    - Constraint Satisfaction
    - Multi-Agent Systems
    - Fuzzy Logic
    - Symbolic AI
    - AI Ethics

## Machine Learning
    - Supervised Learning
    - Unsupervised Learning
    - Reinforcement Learning
    - Deep Learning
    - Neural Networks
    - Statistical Learning
    - Feature Engineering
    - Model Evaluation
    - MLOps
    - AutoML

## Data Science and Analytics
    - Data Mining
    - Statistical Analysis
    - Data Visualization
    - Predictive Analytics
    - Business Intelligence
    - Data Preprocessing
    - Exploratory Data Analysis
    - Time Series Analysis
    - A/B Testing

## Computer Graphics
    - 2D Graphics
    - 3D Graphics
    - Rendering Techniques
    - Computer Animation
    - Image Processing
    - Computational Geometry
    - Virtual Reality
    - Augmented Reality
    - Game Graphics

## Computer Vision
    - Image Recognition
    - Object Detection
    - Face Recognition
    - Medical Imaging
    - Video Analysis
    - Pattern Recognition
    - Image Segmentation
    - Feature Extraction
    - 3D Vision

## Natural Language Processing
    - Text Processing
    - Language Models
    - Machine Translation
    - Speech Recognition
    - Sentiment Analysis
    - Information Extraction
    - Question Answering
    - Text Generation
    - Computational Linguistics

## Robotics
    - Robot Kinematics
    - Robot Dynamics
    - Path Planning
    - Robot Control
    - Computer Vision for Robotics
    - Human-Robot Interaction
    - Autonomous Systems
    - Robot Learning
    - Swarm Robotics

## Human-Computer Interaction
    - User Interface Design
    - User Experience Design
    - Usability Engineering
    - Accessibility
    - Information Visualization
    - Interactive Systems
    - Cognitive Science
    - Social Computing
    - Mobile Interfaces

## Software Engineering
    - Software Development Methodologies
    - Requirements Engineering
    - Software Architecture
    - Software Testing
    - Software Maintenance
    - Version Control
    - DevOps
    - Agile Development
    - Software Quality Assurance
    - Project Management

## Cybersecurity
    - Cryptography
    - Network Security
    - Information Security
    - Application Security
    - System Security
    - Digital Forensics
    - Ethical Hacking
    - Security Protocols
    - Privacy Protection
    - Risk Management

## Web Technologies
    - Web Development
    - Frontend Technologies
    - Backend Technologies
    - Web Services
    - API Design
    - Web Security
    - Web Performance
    - Progressive Web Apps
    - Web Standards

## Mobile Computing
    - Mobile App Development
    - Cross-Platform Development
    - Mobile UI/UX
    - Mobile Security
    - Location-Based Services
    - Mobile Networks
    - Wearable Computing
    - Mobile Game Development

## Game Development
    - Game Design
    - Game Engines
    - Game Physics
    - Game AI
    - Game Graphics
    - Game Audio
    - Multiplayer Systems
    - Game Testing
    - Virtual Worlds

## Computational Science
    - Scientific Computing
    - Numerical Methods
    - Simulation and Modeling
    - High-Performance Computing
    - Computational Physics
    - Computational Chemistry
    - Computational Biology
    - Mathematical Software

## Bioinformatics
    - Sequence Analysis
    - Structural Bioinformatics
    - Genomics
    - Proteomics
    - Systems Biology
    - Phylogenetics
    - Biomedical Informatics
    - Computational Drug Discovery

## Information Systems
    - Management Information Systems
    - Enterprise Systems
    - Business Process Management
    - E-Commerce Systems
    - Decision Support Systems
    - Knowledge Management
    - Information Architecture
    - Digital Transformation

## Emerging Technologies
    - Blockchain Technology
    - Internet of Things
    - Edge Computing
    - Quantum Computing
    - Augmented Reality
    - Virtual Reality
    - 5G Technologies
    - Serverless Computing
    - Neuromorphic Computing

## Example Classifications

Please return the classified results with the JSON format.

Question: According to the Intel Platform Controller Hub EG20T Specification Update Errata #12, what is the root cause of the USB traffic stopping issue related to memory read requests?
Result: {{"main domain": "Computer Architecture", "sub domain": "Hardware Interfaces"}}

###
Now, please classify the given question and only return the JSON.
Here is a new example.

Question: {question}
'''


Programming_Language_Classification = """
You are a programming language classifier. Your task is to analyze the given question and determine which programming language it is primarily about.

## Instructions:
1. Read the question carefully
2. Identify keywords, syntax, libraries, frameworks, or concepts that are specific to a particular programming language
3. Classify the question into one of the following categories:
   - python: Questions about Python syntax, libraries (pandas, numpy, django, etc.), or Python-specific concepts
   - javaScript: Questions about JS syntax, Node.js, React, Vue, browser APIs, etc.
   - java: Questions about Java syntax, Spring, Maven, JVM, etc.
   - cpp: Questions about C++ syntax, STL, memory management, etc.
   - c-sharp: Questions about C# syntax, .NET framework, ASP.NET, etc.
   - go: Questions about Go syntax, goroutines, Go modules, etc.
   - rust: Questions about Rust syntax, ownership, cargo, etc.
   - php: Questions about PHP syntax, Laravel, web development with PHP, etc.
   - ruby: Questions about Ruby syntax, Rails, gems, etc.
   - swift: Questions about Swift syntax, iOS development, etc.
   - kotlin: Questions about Kotlin syntax, Android development, etc.
   - sql: Questions about database queries, MySQL, PostgreSQL, etc.
   - html/css: Questions about web markup and styling
   - r: Questions about R programming, statistics, data analysis
   - matlab: Questions about MATLAB syntax and scientific computing
   - ...
   - others: Questions that don't clearly relate to any specific programming language, or are about general programming concepts, algorithms, or multiple languages without focus on one


## Examples:
Question: "How to create a list in Python?"
Result: {{"Programming Language": "python"}}

Question: "What is a closure in JavaScript?"
Result: {{"Programming Language": "javascript"}}

Question: "How to implement bubble sort?"
Result: {{"Programming Language": "others"}}

Return only the programming language with JSON format.

Now classify the following question:
Question: {question}
Result:
"""


Human_Language_Classification = """
You are a human language classifier. Your task is to determine which human language it is primarily about.

## Examples:
Question: "What Oracle SQL function is used to generate subtotals for all possible combinations of grouped columns?"
Result: {{"Human Language": "English"}}

Question: "在Slicer SALT项目中，用于估计单个受试者时空模型的工具或包是什么？"
Result: {{"Human Language": "Chinese"}}

Return only the human language with JSON format.

Now classify the following question:
Question: {question}
Result:
"""


def get_random_subdomain(domains_dict=None):
    """
    随机从计算机科学知识领域中选取一个子领域
    
    Args:
        domains_dict: 领域字典，默认使用computer_science_domains
    
    Returns:
        tuple: (主领域, 子领域)
    """
    if domains_dict is None:
        domains_dict = COMPUTER_SCIENCE_DOMAINS
    
    # 随机选择一个主领域
    main_domain = random.choice(list(domains_dict.keys()))
    
    # 从该主领域中随机选择一个子领域
    subdomain = random.choice(domains_dict[main_domain])
    
    return main_domain, subdomain

Zh_Evol_CodeSimpleQA = """
你需要根据给定的文档内容生成一个事实性问题和对应的标准答案。要求如下：

1. 生成的问题必须与编程/软件开发领域的客观知识相关。例如可以提问"快速排序在平均情况下的时间复杂度是多少？"。禁止构建涉及个人观点或感受的主观性问题，例如"你如何看待这个框架？"

2. 所提问题必须有且仅有一个明确无争议的答案，且问题不能包含任何形式的模糊性或歧义。例如避免提问"JavaScript中错误处理发生在哪里？"因为范围太宽泛；同样不要问"好代码有哪些特征？"因为这个问题没有具体答案而显得模糊。"最流行的JavaScript框架是什么？"也是个不合格的问题，因为"最流行"可能存在争议。

3. 问题的答案应当具有时间不变性，不会随时间推移而改变。例如"Python当前最新版本是什么？"就不是合适的问题，因为软件版本会随发布而更新。

4. 问题需要具备一定难度以体现挑战性。例如："在MVC模式中，哪个组件负责处理用户输入并更新模型？"

5. 若答案涉及技术术语或缩写，需同时提供完整形式和缩写（如适用），格式为："超文本传输协议（HTTP）"

6. 生成的问题必须与给定的编程类别相关

请以JSON格式返回生成的问题和答案：
{{'question': '在此填入生成的问题', 'answer': '在此填入对应的标准答案'}}

### 示例 ###

### 示例1
类别：数据结构
文档内容：二叉搜索树（BST）是一种层次化数据结构，每个节点最多有两个子节点，分别称为左子节点和右子节点。对每个节点而言，左子树中的所有元素都小于该节点的值，而右子树中的所有元素都大于该节点的值。在平衡二叉搜索树中，搜索、插入和删除操作的平均时间复杂度为O(log n)，其中n是节点数量。

结果：{{'question': '平衡二叉搜索树中搜索操作的平均时间复杂度是多少？', 'answer': 'O(log n)', 'programming language': None}}

### 示例2
类别：编程语言
文档内容：Python使用动态类型，这意味着变量类型是在运行时而非编译时确定的。内置函数type()可用于确定变量的类型。Python还支持鸭子类型，这是一种对象类型或类不如其定义的方法重要的概念。如果一个对象像鸭子一样走路并且像鸭子一样叫，那么它就可以被当作鸭子来对待。

结果：{{'question': '哪个Python内置函数可用于确定变量的类型？', 'answer': 'type()', 'programming language': 'python'}}

###

以下是新示例。

类别：{category}
文档内容：{document}
"""

FILTER_PROMPT = """
You are a question classifier. Your task is to determine if a given question meets two criteria:

Criteria 1: Computer-Related
The question must be related to computers, technology, or digital systems. This includes but is not limited to:

Programming languages, coding, software development
Hardware components, computer architecture
Operating systems, software applications
Networking, internet, web technologies
Databases, data structures, algorithms
Cybersecurity, system administration
Mobile devices, apps, digital platforms
AI/ML, data science, computational topics
Gaming, digital media, computer graphics

Criteria 2: Self-Contained
The question must be self-contained, meaning:

Question: "How do I implement a binary search algorithm in Python?"

All necessary information is provided within the question itself
No external context, files, or previous conversation history is required
The question can be understood and answered independently
No ambiguous references to "this", "that", "the above", etc. without clear antecedents

### Examples ###

### Example 1
Question: How do I implement a binary search algorithm in Python?
Explanation:
    - Computer-related: YES - Programming algorithm implementation
    - Self-contained: YES - All necessary information provided
Result: {{"computer_related": "Yes", "self_contained": "Yes"}}

### Example 2
Explanation:
Question: Why isn't this code working?
Explnation:
    - Computer-related: YES - Programming/debugging question
    - Self-contained: NO - References "this code" without providing the actual code
Result: {{"computer_related": "Yes", "self_contained": "No"}}

### Example 3
Question: What's the best recipe for chocolate cake?
Explanation:
    - Computer-related: NO - Cooking/recipe question
    - Self-contained: YES - Question is complete
Result: {{"computer_related": "No", "self_contained": "Yes"}}


####
Now, please classify the given question and only return the JSON.

Question: {question}
Result: 
"""


En_Evol_CodeSimpleQA = """
You need to generate a factual question and corresponding standard answer based on the given documentation. The requirements are as follows:

1. The generated question must relate to objective knowledge in the programming/software development domain. For example, you can ask 'What is the time complexity of quicksort in the average case?' You must not construct subjective questions involving personal opinions or feelings, such as 'What do you think about this framework?'

2. The proposed question should have one and only one clear and undisputed answer, and the question should not contain any form of ambiguity or vagueness. For example, avoid asking 'Where does error handling occur in JavaScript?' because it's too broad; similarly, don't ask 'What are the characteristics of good code?' because this question is too vague without a specific answer. 'What is the most popular JavaScript framework?' is also an unqualified question because 'most popular' could be controversial.

3. The answer to the question should be time-invariant and will not change over time. For example, 'What is the current latest version of Python?' is not a suitable question because software versions change with releases.

4. The question should have a certain level of difficulty to demonstrate some challenge. For example: 'In the MVC pattern, which component is responsible for handling user input and updating the model?'

5. If the answer involves technical terms or acronyms, provide both the full form and abbreviation where applicable, formatted as: 'Hypertext Transfer Protocol (HTTP)'.

6. The generated question needs to be related to the given programming category.

Please return the generated question and answer in JSON format as follows:
{{'question': 'Fill in the generated question here', 'answer': 'Fill in the corresponding standard answer here'}}

### Examples ###

### Example 1
Category: Data Structures
Document Content: A binary search tree (BST) is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. For each node, all elements in the left subtree are less than the node's value, and all elements in the right subtree are greater than the node's value. The average time complexity for search, insertion, and deletion operations in a balanced BST is O(log n), where n is the number of nodes.

Result: {{'question': 'What is the average time complexity for search operations in a balanced binary search tree?', 'answer': 'O(log n)', 'programming language': None}}

### Example 2
Category: Programming Languages
Document Content: Python uses dynamic typing, which means that variable types are determined at runtime rather than compile time. The built-in function type() can be used to determine the type of a variable. Python also supports duck typing, a concept where the type or class of an object is less important than the methods it defines. If an object walks like a duck and quacks like a duck, then it can be treated as a duck.

Result: {{'question': 'What built-in Python function is used to determine the type of a variable?', 'answer': 'type()', 'programming language': 'python'}}

###

Here is a new example.

Category: {category}
Document Content: {document}
"""

Code_Judgment_En = """
Your job is to look at a code-related question, a gold target answer, and a predicted answer, and then assign a grade of either ['CORRECT', 'INCORRECT', 'NOT_ATTEMPTED'].
First, I will give examples of each grade, and then you will grade a new example.


The following are examples of CORRECT predicted answers.
```
Question: What is the time complexity of searching for an element in a balanced binary search tree?
Gold target: O(log n)
Predicted answer 1: O(log n)
Predicted answer 2: The time complexity is O(log n) because we can eliminate half of the remaining nodes at each step
Predicted answer 3: logarithmic time complexity, which is O(log n)
Predicted answer 4: I believe it's O(log n), though I'd need to double-check the exact analysis
```
These predicted answers are all CORRECT because:
- They contain the essential information from the gold target.
- They do not contradict the gold target with incorrect statements.
- Different notations for the same concept are acceptable (e.g., "logarithmic" vs "O(log n)").
- Additional correct explanations are permissible.
- Hedging is acceptable as long as the core answer is correct and no contradictory information is provided.


The following are examples of INCORRECT predicted answers.
```
Question: What is the time complexity of searching for an element in a balanced binary search tree?
Gold target: O(log n)
Predicted answer 1: O(n)
Predicted answer 2: O(log n) for insertion, but O(n) for search
Predicted answer 3: It's either O(log n) or O(n), depending on the implementation
Predicted answer 4: I think it might be O(1) in the best case, or possibly O(log n)
Predicted answer 5: The complexity could be O(n log n) due to the tree structure
```
These predicted answers are all INCORRECT because:
- They contain factually wrong statements that contradict the gold target.
- Incorrect statements remain incorrect even with hedging language.
- Mixing correct and incorrect information in the same answer makes it incorrect.


The following are examples of NOT_ATTEMPTED predicted answers.
```
Question: What is the time complexity of searching for an element in a balanced binary search tree?
Gold target: O(log n)
Predicted answer 1: I don't know.
Predicted answer 2: I would need to research this to give you an accurate answer.
Predicted answer 3: It depends on the specific type of binary search tree you're referring to.
Predicted answer 4: The time complexity varies based on the tree's balance, but I can't recall the exact value.
```
These predicted answers are all NOT_ATTEMPTED because:
- The essential information from the gold target is not provided.
- No statements contradict the gold target.

Additional grading guidelines for code knowledge questions:
- For questions about syntax, exact syntax matters unless the question asks for conceptual understanding.
- For example, if asked "How do you declare a variable in Python?" with gold target "variable_name = value", answers like "var variable_name = value" would be INCORRECT due to wrong syntax.
- For conceptual questions, different but equivalent explanations are acceptable.
- For example, "recursion" and "a function calling itself" would both be correct for appropriate questions.
- For questions about specific values (like array indices, counts, etc.), the answer must be numerically correct.
- For questions about code output or behavior, the predicted answer must match the expected result exactly.
- For questions asking for code examples, the code must be syntactically correct and solve the problem as specified.
- Minor typos in variable names or keywords that don't affect meaning may be acceptable in conceptual discussions but not in syntax-specific questions.
- For questions about best practices or conventions, answers should align with widely accepted standards in the relevant language/framework.


Here is a new example. Simply reply with either CORRECT, INCORRECT, NOT ATTEMPTED. Don't
apologize or correct yourself if there was a mistake; we are just trying to grade the
answer.
```
Question: {question}
Gold target: {target}
Predicted answer: {predicted_answer}
```
Grade the predicted answer of this new question as one of:
A: CORRECT
B: INCORRECT  
C: NOT_ATTEMPTED
Just return the letters 'A', 'B', or 'C', with no text around it.
"""


Code_Judgment_En = """
Your job is to look at a code-related question, a gold target answer, and a predicted answer, and then assign a grade of either ['CORRECT', 'INCORRECT', 'NOT_ATTEMPTED'].
First, I will give examples of each grade, and then you will grade a new example.


The following are examples of CORRECT predicted answers.
[BEGIN_OF_SAMPLE]
Question: What is the time complexity of searching for an element in a balanced binary search tree?
Gold target: O(log n)
Predicted answer 1: O(log n)
Predicted answer 2: The time complexity is O(log n) because we can eliminate half of the remaining nodes at each step
Predicted answer 3: logarithmic time complexity, which is O(log n)
Predicted answer 4: I believe it's O(log n), though I'd need to double-check the exact analysis
[END_OF_SAMPLE]
These predicted answers are all CORRECT because:
- They contain the essential information from the gold target.
- They do not contradict the gold target with incorrect statements.
- Different notations for the same concept are acceptable (e.g., "logarithmic" vs "O(log n)").
- Additional correct explanations are permissible.
- Hedging is acceptable as long as the core answer is correct and no contradictory information is provided.


The following are examples of INCORRECT predicted answers.
[BEGIN_OF_SAMPLE]
Question: What is the time complexity of searching for an element in a balanced binary search tree?
Gold target: O(log n)
Predicted answer 1: O(n)
Predicted answer 2: O(log n) for insertion, but O(n) for search
Predicted answer 3: It's either O(log n) or O(n), depending on the implementation
Predicted answer 4: I think it might be O(1) in the best case, or possibly O(log n)
Predicted answer 5: The complexity could be O(n log n) due to the tree structure
[END_OF_SAMPLE]
These predicted answers are all INCORRECT because:
- They contain factually wrong statements that contradict the gold target.
- Incorrect statements remain incorrect even with hedging language.
- Mixing correct and incorrect information in the same answer makes it incorrect.


The following are examples of NOT_ATTEMPTED predicted answers.
[BEGIN_OF_SAMPLE]
Question: What is the time complexity of searching for an element in a balanced binary search tree?
Gold target: O(log n)
Predicted answer 1: I don't know.
Predicted answer 2: I would need to research this to give you an accurate answer.
Predicted answer 3: It depends on the specific type of binary search tree you're referring to.
Predicted answer 4: The time complexity varies based on the tree's balance, but I can't recall the exact value.
[END_OF_SAMPLE]
These predicted answers are all NOT_ATTEMPTED because:
- The essential information from the gold target is not provided.
- No statements contradict the gold target.

Additional grading guidelines for code knowledge questions:
- For questions about syntax, exact syntax matters unless the question asks for conceptual understanding.
- For example, if asked "How do you declare a variable in Python?" with gold target "variable_name = value", answers like "var variable_name = value" would be INCORRECT due to wrong syntax.
- For conceptual questions, different but equivalent explanations are acceptable.
- For example, "recursion" and "a function calling itself" would both be correct for appropriate questions.
- For questions about specific values (like array indices, counts, etc.), the answer must be numerically correct.
- For questions about code output or behavior, the predicted answer must match the expected result exactly.
- For questions asking for code examples, the code must be syntactically correct and solve the problem as specified.
- Minor typos in variable names or keywords that don't affect meaning may be acceptable in conceptual discussions but not in syntax-specific questions.
- For questions about best practices or conventions, answers should align with widely accepted standards in the relevant language/framework.


Here is a new example. Simply reply with either CORRECT, INCORRECT, NOT ATTEMPTED. Don't
apologize or correct yourself if there was a mistake; we are just trying to grade the
answer.
[BEGIN_OF_SAMPLE]
Question: {question}
Gold target: {target}
Predicted answer: {predicted_answer}
[END_OF_SAMPLE]
Grade the predicted answer of this new question as one of:
A: CORRECT
B: INCORRECT  
C: NOT_ATTEMPTED
Just return the letters 'A', 'B', or 'C', with no text around it.
"""

Code_Judgment_Zh = """
你的任务是查看一个与代码相关的问题、一个黄金标准答案和一个预测答案，然后给出['CORRECT', 'INCORRECT', 'NOT_ATTEMPTED']其中一个等级。
首先，我会给出每个等级的示例，然后你需要对一个新示例进行评分。

以下是CORRECT预测答案的示例。
[BEGIN_OF_SAMPLE]
问题：在平衡二叉搜索树中搜索元素的时间复杂度是什么？
黄金标准：O(log n)
预测答案1：O(log n)
预测答案2：时间复杂度是O(log n)，因为我们可以在每一步消除一半的剩余节点
预测答案3：对数时间复杂度，即O(log n)
预测答案4：我认为是O(log n)，不过我需要再次确认具体的分析
[END_OF_SAMPLE]
这些预测答案都是CORRECT，因为：
- 它们包含了黄金标准中的基本信息。
- 它们没有与黄金标准相矛盾的错误陈述。
- 同一概念的不同表示法是可以接受的（如"对数"与"O(log n)"）。
- 额外的正确解释是允许的。
- 只要核心答案正确且没有提供矛盾信息，保留性表述是可以接受的。

以下是INCORRECT预测答案的示例。
[BEGIN_OF_SAMPLE]
问题：在平衡二叉搜索树中搜索元素的时间复杂度是什么？
黄金标准：O(log n)
预测答案1：O(n)
预测答案2：插入的时间复杂度是O(log n)，但搜索是O(n)
预测答案3：根据实现方式，要么是O(log n)要么是O(n)
预测答案4：我认为最好情况下可能是O(1)，或者可能是O(log n)
预测答案5：由于树结构，复杂度可能是O(n log n)
[END_OF_SAMPLE]
这些预测答案都是INCORRECT，因为：
- 它们包含与黄金标准相矛盾的事实性错误陈述。
- 即使使用保留性语言，错误陈述仍然是错误的。
- 在同一答案中混合正确和错误信息使其成为错误答案。

以下是NOT_ATTEMPTED预测答案的示例。
[BEGIN_OF_SAMPLE]
问题：在平衡二叉搜索树中搜索元素的时间复杂度是什么？
黄金标准：O(log n)
预测答案1：我不知道。
预测答案2：我需要研究一下才能给你准确答案。
预测答案3：这取决于你指的是哪种特定类型的二叉搜索树。
预测答案4：时间复杂度根据树的平衡性而变化，但我记不起确切的值。
[END_OF_SAMPLE]
这些预测答案都是NOT_ATTEMPTED，因为：
- 没有提供黄金标准中的基本信息。
- 没有与黄金标准相矛盾的陈述。

代码知识问题的额外评分指南：
- 对于语法问题，除非问题询问概念理解，否则确切的语法很重要。
- 例如，如果问"如何在Python中声明变量？"黄金标准是"variable_name = value"，像"var variable_name = value"这样的答案由于语法错误会被判为INCORRECT。
- 对于概念性问题，不同但等价的解释是可以接受的。
- 例如，对于适当的问题，"递归"和"函数调用自身"都是正确的。
- 对于关于特定值的问题（如数组索引、计数等），答案必须在数值上正确。
- 对于关于代码输出或行为的问题，预测答案必须与预期结果完全匹配。
- 对于要求代码示例的问题，代码必须在语法上正确并按规定解决问题。
- 在概念讨论中，不影响含义的变量名或关键字中的小错误可能是可以接受的，但在特定语法问题中不行。
- 对于关于最佳实践或约定的问题，答案应与相关语言/框架中广泛接受的标准保持一致。

这里是一个新示例。简单回复CORRECT、INCORRECT或NOT ATTEMPTED其中之一。不要道歉或纠正自己如果有错误；我们只是试图给答案评分。
[BEGIN_OF_SAMPLE]
问题：{question}
黄金标准：{target}
预测答案：{predicted_answer}
[END_OF_SAMPLE]
将这个新问题的预测答案评为以下之一：
A：CORRECT
B：INCORRECT  
C：NOT_ATTEMPTED
只返回字母'A'、'B'或'C'，周围不要有任何文字。
"""

calibration_zh_prompt = '''
{question}
请基于此问题提供你的最佳答案,并用0到100的分数表示你对该答案的信心（置信度）。请以如下的JSON格式给出回复：
{{
"answer": "你的答案",
"confidence score": "你的置信度"
}}
'''

calibration_en_prompt = '''
{question}
Please provide your best answer to this question, along with a confidence score from 0 to 100 indicating how confident you are in your answer. Please respond in the following JSON format:
{{
"answer": "your answer",
"confidence score": "your confidence score"
}}
'''