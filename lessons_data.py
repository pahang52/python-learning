DATA = [
    {
        "title": "Beginner",
        "color": (0.20, 0.55, 1.0, 1.0),
        "lessons": [
            {
                "title": "Print & Hello World",
                "content": "Python is a simple and powerful language.\nUse print to show text.\n\nprint('Hello World')",
                "quiz": [
                    {
                        "q": "Which command prints text?",
                        "options": ["print()", "echo()", "show()", "write()"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Print the text 'Hello World' using print.",
                    "code": "# complete the code\n",
                    "expected": "Hello World"
                }
            },
            {
                "title": "Variables",
                "content": "Variables store values.\n\nname = 'Python'\nprint(name)",
                "quiz": [
                    {
                        "q": "Which line creates a string variable?",
                        "options": ["name = 'Python'", "name == 'Python'", "'Python' = name", "string name"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Create a variable named name with value 'Python' and print it.",
                    "code": "name = ...\nprint(name)\n",
                    "expected": "Python"
                }
            },
            {
                "title": "Numbers & Operators",
                "content": "You can add, subtract and multiply numbers.\n\nprint(7 + 3)",
                "quiz": [
                    {
                        "q": "What is the output of print(7 + 3)?",
                        "options": ["73", "10", "7+3", "Error"],
                        "answer": 1
                    }
                ],
                "exercise": {
                    "task": "Print the result of 7 + 3.",
                    "code": "print(...)\n",
                    "expected": "10"
                }
            },
            {
                "title": "Strings",
                "content": "Strings are texts inside quotes.\n\ntext = 'python'\nprint(text.upper())",
                "quiz": [
                    {
                        "q": "What is the output of text.upper() for text = 'python'?",
                        "options": ["python", "PYTHON", "Python", "error"],
                        "answer": 1
                    }
                ],
                "exercise": {
                    "task": "Use upper() to make 'python' uppercase and print it.",
                    "code": "text = 'python'\nprint(text.upper())\n",
                    "expected": "PYTHON"
                }
            }
        ]
    },
    {
        "title": "Intermediate",
        "color": (0.20, 0.75, 0.45, 1.0),
        "lessons": [
            {
                "title": "If Statements",
                "content": "Use if to make decisions.\n\nage = 18\nif age >= 18:\n    print('Adult')",
                "quiz": [
                    {
                        "q": "Which keyword checks a condition?",
                        "options": ["if", "loop", "def", "import"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "If age is 18 or more, print 'Adult'.",
                    "code": "age = 18\nif age >= 18:\n    print('Adult')\n",
                    "expected": "Adult"
                }
            },
            {
                "title": "For Loops",
                "content": "The for loop repeats work.\n\nfor i in range(3):\n    print(i)",
                "quiz": [
                    {
                        "q": "Which numbers does range(3) give?",
                        "options": ["0, 1, 2", "1, 2, 3", "0, 1, 2, 3", "only 3"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Use a for loop to print 0 to 2.",
                    "code": "for i in range(3):\n    print(i)\n",
                    "expected": "0 1 2"
                }
            },
            {
                "title": "While Loops",
                "content": "The while loop repeats while a condition is true.\n\ni = 0\nwhile i < 3:\n    print(i)\n    i += 1",
                "quiz": [
                    {
                        "q": "Which loop repeats while a condition is true?",
                        "options": ["while", "if", "def", "class"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Use a while loop to print 0 to 2.",
                    "code": "i = 0\nwhile i < 3:\n    print(i)\n    i += 1\n",
                    "expected": "0 1 2"
                }
            },
            {
                "title": "Lists",
                "content": "Lists store multiple values.\n\nfruits = ['apple', 'banana']\nprint(len(fruits))",
                "quiz": [
                    {
                        "q": "What is the output of len(['apple', 'banana'])?",
                        "options": ["1", "2", "3", "Error"],
                        "answer": 1
                    }
                ],
                "exercise": {
                    "task": "Print the length of the fruits list.",
                    "code": "fruits = ['apple', 'banana']\nprint(len(fruits))\n",
                    "expected": "2"
                }
            }
        ]
    },
    {
        "title": "Advanced",
        "color": (0.70, 0.30, 0.90, 1.0),
        "lessons": [
            {
                "title": "Functions",
                "content": "Functions are reusable code blocks.\n\ndef add(a, b):\n    return a + b\n\nprint(add(2, 3))",
                "quiz": [
                    {
                        "q": "Which keyword defines a function?",
                        "options": ["def", "func", "function", "make"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Create add() that sums two numbers and print add(2, 3).",
                    "code": "def add(a, b):\n    return a + b\n\nprint(add(2, 3))\n",
                    "expected": "5"
                }
            },
            {
                "title": "Dictionaries",
                "content": "Dictionaries store key-value pairs.\n\nuser = {'name': 'Ali'}\nprint(user['name'])",
                "quiz": [
                    {
                        "q": "What is the output of user['name']?",
                        "options": ["name", "Ali", "user", "Error"],
                        "answer": 1
                    }
                ],
                "exercise": {
                    "task": "Print the value of the name key from the user dictionary.",
                    "code": "user = {'name': 'Ali'}\nprint(user['name'])\n",
                    "expected": "Ali"
                }
            },
            {
                "title": "Classes",
                "content": "Use class to create objects.\n\nclass Hero:\n    def __init__(self, name):\n        self.name = name\n\nh = Hero('Arash')\nprint(h.name)",
                "quiz": [
                    {
                        "q": "Which keyword creates a class?",
                        "options": ["class", "def", "object", "new"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Create a Hero class and print the name 'Arash'.",
                    "code": "class Hero:\n    def __init__(self, name):\n        self.name = name\n\nh = Hero('Arash')\nprint(h.name)\n",
                    "expected": "Arash"
                }
            },
            {
                "title": "Error Handling",
                "content": "Use try/except to handle errors.\n\ntry:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Error')",
                "quiz": [
                    {
                        "q": "Which structure handles errors?",
                        "options": ["try/except", "loop", "import", "print"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Catch a division by zero and print 'Error'.",
                    "code": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Error')\n",
                    "expected": "Error"
                }
            }
        ]
    },
    {
        "title": "Pro",
        "color": (0.90, 0.25, 0.35, 1.0),
        "lessons": [
            {
                "title": "List Comprehension",
                "content": "List comprehension builds lists quickly.\n\nsquares = [x * x for x in range(3)]\nprint(squares)",
                "quiz": [
                    {
                        "q": "What is the output of [x * x for x in range(3)]?",
                        "options": ["[0, 1, 4]", "[1, 4, 9]", "[0, 1, 2]", "Error"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Build and print the squares of 0 to 2.",
                    "code": "squares = [x * x for x in range(3)]\nprint(squares)\n",
                    "expected": "[0, 1, 4]"
                }
            },
            {
                "title": "Lambda",
                "content": "Lambda is a small anonymous function.\n\ndouble = lambda x: x * 2\nprint(double(4))",
                "quiz": [
                    {
                        "q": "What does lambda create?",
                        "options": ["a small function", "a class", "a loop", "a file"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Create a lambda that doubles a number and print double(4).",
                    "code": "double = lambda x: x * 2\nprint(double(4))\n",
                    "expected": "8"
                }
            },
            {
                "title": "String Slicing",
                "content": "Use [::-1] to reverse a string.\n\ntext = 'python'\nprint(text[::-1])",
                "quiz": [
                    {
                        "q": "What does text[::-1] do?",
                        "options": ["reverses the string", "deletes the string", "gives the length", "raises an error"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Reverse the string 'python' and print it.",
                    "code": "text = 'python'\nprint(text[::-1])\n",
                    "expected": "nohtyp"
                }
            },
            {
                "title": "Sets",
                "content": "Sets remove duplicate values.\n\nnums = {1, 2, 2, 3}\nprint(len(nums))",
                "quiz": [
                    {
                        "q": "What is the output of len({1, 2, 2, 3})?",
                        "options": ["3", "4", "2", "Error"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "Print the length of a set with duplicate values.",
                    "code": "nums = {1, 2, 2, 3}\nprint(len(nums))\n",
                    "expected": "3"
                }
            }
        ]
    }
]
