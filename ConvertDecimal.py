{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "294bd13d-7ed0-4573-9842-cb3202e57a25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a decimal number:  52\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Octal: 0o64\n",
      "Hexadecimal: 0x34\n",
      "Binary: 0b110100\n"
     ]
    }
   ],
   "source": [
    "\n",
    "decimal_num = int(input(\"Enter a decimal number: \"))\n",
    "\n",
    "octal_num = oct(decimal_num)\n",
    "hexadecimal_num = hex(decimal_num)\n",
    "binary_num = bin(decimal_num)\n",
    "\n",
    "print(f\"Octal: {octal_num}\")\n",
    "print(f\"Hexadecimal: {hexadecimal_num}\")\n",
    "print(f\"Binary: {binary_num}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1f9aefa-093d-4a42-a423-da98db2e32e6",
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
