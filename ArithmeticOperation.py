{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6d926553-62f4-46f1-8d2a-6701d4de2bbf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first integer:  9\n",
      "Enter second integer:  \n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: ''",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m# Read two integer numbers from the user\u001b[39;00m\n\u001b[0;32m      2\u001b[0m num1 \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter first integer: \u001b[39m\u001b[38;5;124m\"\u001b[39m))\n\u001b[1;32m----> 3\u001b[0m num2 \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter second integer: \u001b[39m\u001b[38;5;124m\"\u001b[39m))\n\u001b[0;32m      5\u001b[0m \u001b[38;5;66;03m# Perform arithmetic operations\u001b[39;00m\n\u001b[0;32m      6\u001b[0m addition \u001b[38;5;241m=\u001b[39m num1 \u001b[38;5;241m+\u001b[39m num2\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: ''"
     ]
    }
   ],
   "source": [
    "# Read two integer numbers from the user\n",
    "num1 = int(input(\"Enter first integer: \"))\n",
    "num2 = int(input(\"Enter second integer: \"))\n",
    "\n",
    "# Perform arithmetic operations\n",
    "addition = num1 + num2\n",
    "subtraction = num1 - num2\n",
    "multiplication = num1 * num2\n",
    "division = num1 / num2 if num2 != 0 else \"Undefined (division by zero)\"\n",
    "modulus = num1 % num2 if num2 != 0 else \"Undefined (modulus by zero)\"\n",
    "\n",
    "# Display results\n",
    "print(f\"Addition: {addition}\")\n",
    "print(f\"Subtraction: {subtraction}\")\n",
    "print(f\"Multiplication: {multiplication}\")\n",
    "print(f\"Division: {division}\")\n",
    "print(f\"Modulus: {modulus}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7610d68-0f0e-4e35-b00f-2615add9f2b2",
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
