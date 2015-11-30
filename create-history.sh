tac urls.txt | tr '/' '_' | xargs -n1 -I'{}' sh -c "cp '{}' file && git commit file -m '{}'"
