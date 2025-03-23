{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "717e743f-4434-45ff-b377-8792ff1f4377",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 1 -1 3 -1\n"
     ]
    }
   ],
   "source": [
    "def next_smaller_element(tpl):\n",
    "    result = []\n",
    "    for i in range(len(tpl) - 1):\n",
    "        if tpl[i] > tpl[i + 1]:\n",
    "            result.append(tpl[i + 1])\n",
    "        else:\n",
    "            result.append(-1)\n",
    "    result.append(-1)  # The last element always gets -1\n",
    "    print(\" \".join(map(str, result)))\n",
    "\n",
    "# Example usage\n",
    "tpl = (4, 2, 1, 5, 3)\n",
    "next_smaller_element(tpl)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df58effa-34a0-41cb-b3d5-8d9a7444b722",
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
