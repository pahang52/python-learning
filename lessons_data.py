DATA = [
    {
        "title": "مقدماتی",
        "color": (0.20, 0.55, 1.0, 1.0),
        "lessons": [
            {
                "title": "چاپ و سلام دنیا",
                "content": "پایتون زبانی ساده و قدرتمند است.\nبرای چاپ متن از print استفاده کن.\n\nprint('سلام دنیا')",
                "quiz": [
                    {
                        "q": "کدام دستور متن را چاپ می‌کند؟",
                        "options": ["print()", "echo()", "show()", "write()"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "با print عبارت 'سلام دنیا' را چاپ کن.",
                    "code": "# کد را کامل کن\n",
                    "expected": "سلام دنیا"
                }
            },
            {
                "title": "متغیرها",
                "content": "متغیرها ظرفی برای ذخیره مقدار هستند.\n\nname = 'پایتون'\nprint(name)",
                "quiz": [
                    {
                        "q": "کدام خط یک متغیر رشته می‌سازد؟",
                        "options": ["name = 'پایتون'", "name == 'پایتون'", "'پایتون' = name", "string name"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "متغیری به اسم name با مقدار 'پایتون' بساز و آن را چاپ کن.",
                    "code": "name = ...\nprint(name)\n",
                    "expected": "پایتون"
                }
            },
            {
                "title": "اعداد و عملگرها",
                "content": "در پایتون می‌توانی اعداد را جمع، کم و ضرب کنی.\n\nprint(7 + 3)",
                "quiz": [
                    {
                        "q": "خروجی print(7 + 3) چیست؟",
                        "options": ["73", "10", "7+3", "خطا"],
                        "answer": 1
                    }
                ],
                "exercise": {
                    "task": "حاصل 7 + 3 را چاپ کن.",
                    "code": "print(...)\n",
                    "expected": "10"
                }
            },
            {
                "title": "رشته‌ها",
                "content": "رشته‌ها متن‌هایی هستند که بین علامت نقل قول قرار می‌گیرند.\n\ntext = 'python'\nprint(text.upper())",
                "quiz": [
                    {
                        "q": "خروجی text.upper() برای text = 'python' چیست؟",
                        "options": ["python", "PYTHON", "Python", "پایتون"],
                        "answer": 1
                    }
                ],
                "exercise": {
                    "task": "با متد upper متن 'python' را بزرگ کن و چاپ کن.",
                    "code": "text = 'python'\nprint(text.upper())\n",
                    "expected": "PYTHON"
                }
            }
        ]
    },
    {
        "title": "متوسطه",
        "color": (0.20, 0.75, 0.45, 1.0),
        "lessons": [
            {
                "title": "شرط‌ها",
                "content": "با if می‌توانی شرط بگذاری.\n\nage = 18\nif age >= 18:\n    print('بزرگسال')",
                "quiz": [
                    {
                        "q": "برای بررسی شرط از کدام کلمه استفاده می‌شود؟",
                        "options": ["if", "loop", "def", "import"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "اگر age بزرگ‌تر یا مساوی 18 بود، 'بزرگسال' را چاپ کن.",
                    "code": "age = 18\nif age >= 18:\n    print('بزرگسال')\n",
                    "expected": "بزرگسال"
                }
            },
            {
                "title": "حلقه for",
                "content": "حلقه for کارهای تکراری را انجام می‌دهد.\n\nfor i in range(3):\n    print(i)",
                "quiz": [
                    {
                        "q": "range(3) کدام اعداد را می‌دهد؟",
                        "options": ["0، 1، 2", "1، 2، 3", "0، 1، 2، 3", "فقط 3"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "با for اعداد 0 تا 2 را چاپ کن.",
                    "code": "for i in range(3):\n    print(i)\n",
                    "expected": "0 1 2"
                }
            },
            {
                "title": "حلقه while",
                "content": "حلقه while تا زمانی که شرط درست باشد تکرار می‌شود.\n\ni = 0\nwhile i < 3:\n    print(i)\n    i += 1",
                "quiz": [
                    {
                        "q": "کدام حلقه تا درست بودن شرط تکرار می‌کند؟",
                        "options": ["while", "if", "def", "class"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "با while اعداد 0 تا 2 را چاپ کن.",
                    "code": "i = 0\nwhile i < 3:\n    print(i)\n    i += 1\n",
                    "expected": "0 1 2"
                }
            },
            {
                "title": "لیست‌ها",
                "content": "لیست‌ها چند مقدار را نگه می‌دارند.\n\nfruits = ['سیب', 'موز']\nprint(len(fruits))",
                "quiz": [
                    {
                        "q": "خروجی len(['سیب', 'موز']) چیست؟",
                        "options": ["1", "2", "3", "خطا"],
                        "answer": 1
                    }
                ],
                "exercise": {
                    "task": "طول لیست fruits را چاپ کن.",
                    "code": "fruits = ['سیب', 'موز']\nprint(len(fruits))\n",
                    "expected": "2"
                }
            }
        ]
    },
    {
        "title": "پیشرفته",
        "color": (0.70, 0.30, 0.90, 1.0),
        "lessons": [
            {
                "title": "تابع‌ها",
                "content": "تابع‌ها کدهای قابل استفاده مجدد هستند.\n\ndef add(a, b):\n    return a + b\n\nprint(add(2, 3))",
                "quiz": [
                    {
                        "q": "برای ساخت تابع از کدام کلمه استفاده می‌شود؟",
                        "options": ["def", "func", "function", "make"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "تابع add بساز که دو عدد را جمع کند و نتیجه 5 را چاپ کن.",
                    "code": "def add(a, b):\n    return a + b\n\nprint(add(2, 3))\n",
                    "expected": "5"
                }
            },
            {
                "title": "دیکشنری‌ها",
                "content": "دیکشنری داده را به صورت کلید و مقدار ذخیره می‌کند.\n\nuser = {'name': 'علی'}\nprint(user['name'])",
                "quiz": [
                    {
                        "q": "خروجی user['name'] چیست؟",
                        "options": ["name", "علی", "user", "خطا"],
                        "answer": 1
                    }
                ],
                "exercise": {
                    "task": "مقدار کلید name را از دیکشنری user چاپ کن.",
                    "code": "user = {'name': 'علی'}\nprint(user['name'])\n",
                    "expected": "علی"
                }
            },
            {
                "title": "کلاس‌ها",
                "content": "با class شیء می‌سازی.\n\nclass Hero:\n    def __init__(self, name):\n        self.name = name\n\nh = Hero('آرش')\nprint(h.name)",
                "quiz": [
                    {
                        "q": "برای ساخت کلاس از کدام کلمه استفاده می‌شود؟",
                        "options": ["class", "def", "object", "new"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "یک کلاس Hero بساز و نام 'آرش' را چاپ کن.",
                    "code": "class Hero:\n    def __init__(self, name):\n        self.name = name\n\nh = Hero('آرش')\nprint(h.name)\n",
                    "expected": "آرش"
                }
            },
            {
                "title": "مدیریت خطا",
                "content": "با try و except خطاها را مدیریت می‌کنی.\n\ntry:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('خطا')",
                "quiz": [
                    {
                        "q": "برای مدیریت خطا از کدام ساختار استفاده می‌شود؟",
                        "options": ["try/except", "loop", "import", "print"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "خطای تقسیم بر صفر را بگیر و 'خطا' را چاپ کن.",
                    "code": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('خطا')\n",
                    "expected": "خطا"
                }
            }
        ]
    },
    {
        "title": "حرفه‌ای",
        "color": (0.90, 0.25, 0.35, 1.0),
        "lessons": [
            {
                "title": "List Comprehension",
                "content": "با List Comprehension سریع لیست می‌سازی.\n\nsquares = [x * x for x in range(3)]\nprint(squares)",
                "quiz": [
                    {
                        "q": "خروجی [x * x for x in range(3)] چیست؟",
                        "options": ["[0, 1, 4]", "[1, 4, 9]", "[0, 1, 2]", "خطا"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "لیست مربعات اعداد 0 تا 2 را بساز و چاپ کن.",
                    "code": "squares = [x * x for x in range(3)]\nprint(squares)\n",
                    "expected": "[0, 1, 4]"
                }
            },
            {
                "title": "Lambda",
                "content": "Lambda یک تابع کوتاه و بدون اسم است.\n\ndouble = lambda x: x * 2\nprint(double(4))",
                "quiz": [
                    {
                        "q": "lambda چه چیزی می‌سازد؟",
                        "options": ["تابع کوتاه", "کلاس", "حلقه", "فایل"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "با lambda تابعی بساز که عدد را دو برابر کند و مقدار 4 را چاپ کن.",
                    "code": "double = lambda x: x * 2\nprint(double(4))\n",
                    "expected": "8"
                }
            },
            {
                "title": "برش رشته",
                "content": "با [::-1] می‌توانی یک رشته را برعکس کنی.\n\ntext = 'python'\nprint(text[::-1])",
                "quiz": [
                    {
                        "q": "text[::-1] چه کاری انجام می‌دهد؟",
                        "options": ["رشته را برعکس می‌کند", "رشته را حذف می‌کند", "طول رشته را می‌دهد", "خطا می‌دهد"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "رشته 'python' را برعکس کن و چاپ کن.",
                    "code": "text = 'python'\nprint(text[::-1])\n",
                    "expected": "nohtyp"
                }
            },
            {
                "title": "Set",
                "content": "Set مقدارهای تکراری را حذف می‌کند.\n\nnums = {1, 2, 2, 3}\nprint(len(nums))",
                "quiz": [
                    {
                        "q": "خروجی len({1, 2, 2, 3}) چیست؟",
                        "options": ["3", "4", "2", "خطا"],
                        "answer": 0
                    }
                ],
                "exercise": {
                    "task": "طول یک set با مقدارهای تکراری را چاپ کن.",
                    "code": "nums = {1, 2, 2, 3}\nprint(len(nums))\n",
                    "expected": "3"
                }
            }
        ]
    }
]
