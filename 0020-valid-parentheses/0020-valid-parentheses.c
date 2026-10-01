bool isValid(char* s) {
    int stack[10000];
    int top = -1;
    void push(char s){
        stack[top+1] = s;
        top++;
    }
    char pop(){
        if(top == -1){
            return '#';
        }
        char ch = stack[top];
        top--;
        return ch;
    }
    int matchingpair(char open,char close){
        if(open == '(' && close == ')') return 1;
        else if(open == '{' && close == '}') return 1;
        else if(open == '[' && close == ']') return 1;
        return 0;
    }
    for(int i = 0; s[i] != '\0';i++){
        char ch = s[i]; 
        if( ch == '{' || ch == '[' || ch == '(' ){
            push(ch);
        }else{
            char stacktop =  pop();
            if( stacktop == '#' ||!matchingpair(stacktop,ch)){
                return false;
            }
        }
    }
    if(top != -1){
        return false;
    }else{
        return true;
    }
}