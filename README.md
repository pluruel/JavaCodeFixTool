# Java Code Fix Tool

## 목적

이 툴은 java project에서 일괄적인 수정을 해야할 때, 통상 IDE가 지원하지 않는 범위에서 패턴화가 이루어 졌을 때 사용할 수 있는 툴이다.

## 기능

1. inputpath하위의 모든 파일을 검색한 후,
1. 아래 두가지 상황을 제외하고는 outputpath 하위에 폴더 구조 그대로 복사한다.
- *.class파일은 복사하지 않는다.
- *.java파일은 내부 열어 코드줄을확인한다.
    - find() 메소드로 찾고 replace() 메소드로 해당 영역을 수정하여 기록한다.

## 사용 방법 

1. outputpath와 inputpath를 수정한다
1. cpyandpaste() 메소드 중 다음의 부분을 수정한다
~~~python
else :
    while True:
        line = inf.readline()
    
        if not line: break
            
        # 이 부분을 수정하면 된다. 찾고싶은 라인을 찾고, 원하는 방식으로 변경하면 된다.
        # 객체생성 후 사용하는 메소드를 스태틱 메소드로 변경한 예제.
        elif line.find("new ABC(") > -1:
            line = line.replace("new ABC(", "ABC.run(")
        
        outf.write(line)
~~~

위치만 코드로 잡고 디버깅 환경을 돌리면 잘 나온다.

## 주의사항
- 바뀐코드가 정확한지는 모른다
- 코드를 카피해서 사용하는것을 추천