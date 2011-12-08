hello.txt: hello.py
	python hello.py > hello.txt
	cat hello.txt
	@echo 'or with'
	python hello.py | cat
	@echo 'or'
	python hello.py
.PHONY : clean
clean:
	rm -f hello.txt
