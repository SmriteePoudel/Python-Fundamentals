{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4f85ec8b-36a9-4619-a8ab-6d86d322153e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter old meter reading:  52\n",
      "Enter current meter reading:  96\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total electricity bill: Rs. 176.00\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "# Get meter readings from user\n",
    "old_reading = int(input(\"Enter old meter reading: \"))\n",
    "current_reading = int(input(\"Enter current meter reading: \"))\n",
    "\n",
    "# Calculate consumption units\n",
    "units = current_reading - old_reading\n",
    "bill = 0\n",
    "\n",
    "# Calculate bill based on slab rates\n",
    "if units <= 100:\n",
    "    bill = units * 4\n",
    "elif units <= 150:\n",
    "    bill = (100 * 4) + (units - 100) * 4.6\n",
    "elif units <= 200:\n",
    "    bill = (100 * 4) + (50 * 4.6) + (units - 150) * 5.2\n",
    "elif units <= 300:\n",
    "    bill = (100 * 4) + (50 * 4.6) + (50 * 5.2) + (units - 200) * 6.3\n",
    "else:\n",
    "    bill = (100 * 4) + (50 * 4.6) + (50 * 5.2) + (100 * 6.3) + (units - 300) * 8\n",
    "\n",
    "# Display the electricity bill\n",
    "print(f\"Total electricity bill: Rs. {bill:.2f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a4aec12-4be1-4dd1-9339-a24d38e47c4b",
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
