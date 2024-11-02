function sum_of_squares(n::Int)
    total = 0
    for i in 1:n
        total += i^2
    end
    return total
end

# Main program
println("Enter a number: ")
n = parse(Int, readline())

# Call the function and display the result
result = sum_of_squares(n)
println("The sum of squares from 1 to $n is $result.")