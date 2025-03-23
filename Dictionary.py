{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd9daaf7-f9ae-46fc-8fa5-9deee21ef029",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to read student details into a nested list\n",
    "def read_students(n):\n",
    "    students_list = []\n",
    "    for i in range(n):\n",
    "        print(f\"Enter details for student {i + 1}:\")\n",
    "        name = input(\"Name: \")\n",
    "        age = input(\"Age: \")\n",
    "        grade = input(\"Grade: \")\n",
    "        students_list.append([name, age, grade])\n",
    "    return students_list\n",
    "\n",
    "# Function to convert nested list into nested dictionary\n",
    "def convert_to_dict(students_list):\n",
    "    students_dict = {}\n",
    "    for i, student in enumerate(students_list, start=1):\n",
    "        students_dict[f\"Student_{i}\"] = {\n",
    "            \"Name\": student[0],\n",
    "            \"Age\": student[1],\n",
    "            \"Grade\": student[2]\n",
    "        }\n",
    "    return students_dict\n",
    "\n",
    "# Main function to run the script\n",
    "def main():\n",
    "    n = int(input(\"Enter the number of students: \"))\n",
    "    students_list = read_students(n)\n",
    "    students_dict = convert_to_dict(students_list)\n",
    "    print(\"\\nStudent Details (Nested Dictionary):\")\n",
    "    print(students_dict)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f7d2813-c60c-4a84-aefa-db10aeaa59d7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:anaconda3]",
   "language": "python",
   "name": "conda-env-anaconda3-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
