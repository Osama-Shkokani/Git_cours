{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOfXKFtpMCcy1sPnC0FsigH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Osama-Shkokani/Git_cours/blob/master/Untitled0.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iSKO-v7xEKrB",
        "outputId": "e0a85fc0-0864-476c-f0fe-31860502b8fd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--- Start of Homework #2 Solutions ---\n",
            "\n",
            "Q1: Element at (3rd row, 1st col): 70\n",
            "Q2: Second column: [20 50 80]\n",
            "Q3: Data type: int64\n",
            "Q4: Original after modifying copy (should remain 10): 10\n",
            "Q5: Original after modifying view (changed to 555): 555\n",
            "Q6: Shape of array: (3, 3)\n",
            "Q7: Loop output:\n",
            "    Position (0, 0): 10\n",
            "    Position (0, 1): 20\n",
            "    Position (0, 2): 30\n",
            "    Position (1, 0): 40\n",
            "    Position (1, 1): 50\n",
            "    Position (1, 2): 60\n",
            "    Position (2, 0): 70\n",
            "    Position (2, 1): 80\n",
            "    Position (2, 2): 90\n",
            "Q8: Vertical Stack Shape: (6, 3)\n",
            "    Horizontal Stack Shape: (3, 6)\n",
            "Q9: Split (first sub-array): [10 40 70]\n",
            "Q10: Position of 60 is Row: 1, Col: 2\n",
            "Q11: Sorted row example: [10 20 30]\n",
            "Q12: Elements > 50: [60 70 80 90]\n",
            "Q13: Random 2x3:\n",
            " [[45 43 14]\n",
            " [49 90  4]]\n",
            "Q14: Sqrt of first row: [3.16 4.47 5.48]\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "\n",
        "# --- تعريف المصفوفة الأساسية كما وردت في الواجب ---\n",
        "arr = np.array([[10, 20, 30],\n",
        "                [40, 50, 60],\n",
        "                [70, 80, 90]])\n",
        "\n",
        "print(\"--- Start of Homework #2 Solutions ---\\n\")\n",
        "\n",
        "# 1. Indexing: Print element in 3rd row and 1st column\n",
        "print(\"Q1: Element at (3rd row, 1st col):\", arr[2, 0])\n",
        "\n",
        "# 2. Slicing: Print the second column\n",
        "print(\"Q2: Second column:\", arr[:, 1])\n",
        "\n",
        "# 3. Print data type\n",
        "print(\"Q3: Data type:\", arr.dtype)\n",
        "\n",
        "# 4. Copy: Modify copy and check original\n",
        "arr_copy = arr.copy()\n",
        "arr_copy[0, 0] = 999\n",
        "print(\"Q4: Original after modifying copy (should remain 10):\", arr[0, 0])\n",
        "\n",
        "# 5. View: Modify view and check original\n",
        "arr_view = arr.view()\n",
        "arr_view[0, 0] = 555\n",
        "print(f\"Q5: Original after modifying view (changed to {arr[0,0]}):\", arr[0, 0])\n",
        "arr[0, 0] = 10 # إعادة القيمة الأصلية لتكملة الحل\n",
        "\n",
        "# 6. Print Shape\n",
        "print(\"Q6: Shape of array:\", arr.shape)\n",
        "\n",
        "# 7. Loop: Print element with position\n",
        "print(\"Q7: Loop output:\")\n",
        "for (row, col), value in np.ndenumerate(arr):\n",
        "    print(f\"    Position ({row}, {col}): {value}\")\n",
        "\n",
        "# 8. Join: Vertical & Horizontal\n",
        "new_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
        "print(\"Q8: Vertical Stack Shape:\", np.vstack((arr, new_arr)).shape)\n",
        "print(\"    Horizontal Stack Shape:\", np.hstack((arr, new_arr)).shape)\n",
        "\n",
        "# 9. Split: Split into 3 arrays\n",
        "print(\"Q9: Split (first sub-array):\", np.hsplit(arr, 3)[0].flatten())\n",
        "\n",
        "# 10. Search: Position of 60\n",
        "res = np.where(arr == 60)\n",
        "print(f\"Q10: Position of 60 is Row: {res[0][0]}, Col: {res[1][0]}\")\n",
        "\n",
        "# 11. Sort rows\n",
        "print(\"Q11: Sorted row example:\", np.sort(np.array([30, 10, 20])))\n",
        "\n",
        "# 12. Filter > 50\n",
        "print(\"Q12: Elements > 50:\", arr[arr > 50])\n",
        "\n",
        "# 13. Random Array 2x3\n",
        "print(\"Q13: Random 2x3:\\n\", np.random.randint(1, 100, (2, 3)))\n",
        "\n",
        "# 14. ufunc (Square Root)\n",
        "print(\"Q14: Sqrt of first row:\", np.round(np.sqrt(arr[0]), 2))"
      ]
    }
  ]
}