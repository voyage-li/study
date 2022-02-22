## Missing-Semester

课程主页: [Missing-Semester](https://missing.csail.mit.edu/2020/)

放了一些个人配置，[个人 fish shell 使用过程记录](https://voyage-li.github.io/2022/01/25/fish-shell/)

没有完全听完,**这些东西感觉还是用的时候查比较有学习欲望**

fish shell 语法样例

```sh
function test_if
    if [ (count $argv) -eq 0 ]
        echo "false"
    else if [ "$argv[1]" -eq "$argv[2]" ]
        echo $argv[1] "==" $argv[2]
    else
        echo $argv[1] "!=" $argv[2]
    end
end

function test_switch
    for string in $argv
        switch $string
            case "switch"
                echo "this is switch"
            case "if"
                echo "this is if"
            case "while"
                echo "this is while"
            case '*'
                echo "none"
        end
    end
end

function test_while
    while true
        echo "fish shell"
    end
end

```
