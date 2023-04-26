#!/usr/bin/python3
""" base.py """

import json


class Base():
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init """
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, val):
        if val is None:
            Base.__nb_objects += 1
            self.__id = self.__nb_objects
        else:
            self.__id = val

    @staticmethod
    def to_json_string(list_dictionaries):
        """Doc"""
        if list_dictionaries is None or \
                len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json rep to a file """
        objs_dict_rep = []

        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None or len(list_objs) < 1:
                f.write("[]")
                return

            for obj in list_objs:
                objs_dict_rep.append(obj.to_dictionary())
            f.write(cls.to_json_string(objs_dict_rep))

    @staticmethod
    def from_json_string(json_string):
        """ return list of json string """
        if json_string is None or len(json_string) < 1:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an updated instance with all attributes """
        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 6)
        elif cls.__name__ == 'Square':
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from file"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                serialized_content = file.read()
        except FileNotFoundError:
            return list()

        deserialized_content = cls.from_json_string(serialized_content)

        instances_list = []
        for instance_dict in deserialized_content:
            instances_list.append(cls.create(**instance_dict))
        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save to a CSV file """

        fn = cls.__name__ + ".csv"
        if fn == "Rectangle.csv":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(fn, mode="w", newline="") as myFile:
            if list_objs is None:
                writer = csv.writer(myFile)
                writer.writerow([[]])
            else:
                writer = csv.DictWriter(myFile, fieldnames=fields)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load from a CSV file """
        try:
            fn = cls.__name__ + ".csv"
            with open(fn, newline="") as myFile:
                reader = csv.DictReader(myFile)
                lst = []
                for x in reader:
                    for i, n in x.items():
                        x[i] = int(n)
                    lst.append(x)
                return ([cls.create(**objt) for objt in lst])
        except FileNotFoundError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw the rectangles and squares """
        shapes = []
        if list_rectangles:
            shapes.extend(list_rectangles)
        if list_squares:
            shapes.extend(list_squares)
        pen = turtle.Turtle()
        pen.pen(pencolor='black', pendown=False, pensize=2, shown=False)
        for shape in shapes:
            pen.penup()
            pen.setpos(shape.x, shape.y)
            pen.pendown()
            pen.forward(shape.width)
            pen.right(90)
            pen.forward(shape.height)
            pen.right(90)
            pen.forward(shape.width)
            pen.right(90)
            pen.forward(shape.height)
            pen.right(90)
