#include <cstdio>
#include <climits> 
#include <vector>

int main(){
    // Using a deleted pointer
    int* deleted_pointer = new int;
    delete deleted_pointer;
    *deleted_pointer = 10; 

    // Dereferencing a null pointer
    int* dereference_null_pointer = nullptr;
    *dereference_null_pointer = 10; 

    // Memory leak if delete is not called
    int* memory_leak_pointer = new int;

    // Division by zero
    int a = 10, b = 0;
    int division_by_zero = a / b; 

    // Shifting more bits than the size of int
    int num1 = 10;
    int shift_count_overflow = num1 << 50; 

    // Accessing an element out of bounds in STL
    std::vector<int> vec;
    int element_out_of_bounds1 = vec.at(10); 

    // Accessing an element out of bounds
    int arr[5] = {1, 2, 3, 4, 5};
    int element_out_of_bounds2 = arr[10]; 

    // Using uninitialized variable
    int value3;
    int uninitialized_variable = value3 + 10; 

    return 0;
}