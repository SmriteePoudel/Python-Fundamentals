{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3b21a669-9a0a-4473-9ca1-ac55757db0aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "1 2 1 \n",
      "1 2 3 2 1 \n",
      "1 2 3 4 3 2 1 \n",
      "1 2 3 4 5 4 3 2 1 \n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "n = 5  \n",
    "\n",
    "for i in range(1, n + 1):\n",
    "    \n",
    "    for j in range(1, i + 1):\n",
    "        print(j, end=\" \")\n",
    "    \n",
    "    for j in range(i - 1, 0, -1):\n",
    "        print(j, end=\" \")\n",
    "    print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c760daaa-eb05-4132-a7cd-35b8e3e1710e",
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
