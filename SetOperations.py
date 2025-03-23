{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5830b3e4-b85e-412c-afe3-871a5609d2b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After update set1: {1, 2, 3, 4, 5, 6, 7, 8}\n",
      "After discard set1: {1, 2, 4, 5}\n",
      "Is set1 a superset of {1,2}: True\n",
      "Are set1 and set2 disjoint? False\n",
      "Symmetric Difference between set1 and set2: {1, 2, 6, 7, 8}\n"
     ]
    }
   ],
   "source": [
    "# Define two sets\n",
    "set1 = {1, 2, 3, 4, 5}\n",
    "set2 = {4, 5, 6, 7, 8}\n",
    "\n",
    "# i) update() \n",
    "set1.update(set2)\n",
    "print(\"After update set1:\", set1)  # set1 now contains all elements from both sets\n",
    "\n",
    "# Reset set1\n",
    "set1 = {1, 2, 3, 4, 5}\n",
    "\n",
    "# ii) discard() - Removes an element if it exists, does nothing otherwise\n",
    "set1.discard(3)\n",
    "print(\"After discard set1:\", set1)  # Element 3 is removed\n",
    "\n",
    "# iii) issuperset() - Checks if a set contains all elements of another set\n",
    "print(\"Is set1 a superset of {1,2}:\", set1.issuperset({1, 2}))\n",
    "\n",
    "# iv) isdisjoint() - Checks if two sets have no elements in common\n",
    "print(\"Are set1 and set2 disjoint?\", set1.isdisjoint(set2))\n",
    "\n",
    "# v) symmetric_difference() - Returns elements present in either of the sets but not both\n",
    "sym_diff = set1.symmetric_difference(set2)\n",
    "print(\"Symmetric Difference between set1 and set2:\", sym_diff)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6719489-61e8-41ca-8461-b6c60e6156fc",
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
