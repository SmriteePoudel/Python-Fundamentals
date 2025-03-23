{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f58a2995-ea71-4e15-b016-c7e25610f4d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 cannot be expressed as a power of 2.\n"
     ]
    }
   ],
   "source": [
    "def is_power_of_two(n):\n",
    "    if n <= 0:\n",
    "        return False\n",
    "    return (n & (n - 1)) == 0\n",
    "\n",
    "# Example usage\n",
    "N = int(input(\"Enter a number: \"))\n",
    "if is_power_of_two(N):\n",
    "    print(f\"{N} can be expressed as a power of 2.\")\n",
    "else:\n",
    "    print(f\"{N} cannot be expressed as a power of 2.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ea79e1e-a8f8-42d3-aa9d-507d99a0401f",
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
