{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1b46f4c-cc1a-46d8-8e6d-41be0bc36dba",
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter\n",
    "\n",
    "def count_eye_occurrences(input_string):\n",
    "    # Count the frequency of each character in the input string\n",
    "    char_count = Counter(input_string)\n",
    "    \n",
    "    # \"eye\" consists of 'e' twice and 'y' once\n",
    "    count_eye = min(char_count.get('e', 0) // 2, char_count.get('y', 0))\n",
    "    \n",
    "    return count_eye\n",
    "\n",
    "# Example usage\n",
    "input_string = \"acdfksekfevskdbmzsubaobeubrfaywibauadzqwekljfs\"\n",
    "print(\"Number of times 'eye' can be formed:\", count_eye_occurrences(input_string))\n",
    "\n"
   ]
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
