from blog.forms import SearchForm
from django.views.generic.edit import FormView
from blog.models import Post

class SearchFormView():
    form_class = SearchForm 
    template_name = 'search.html' 
    
    def form_valid(self, form): 
        # post method로 값이 전달 됬을 경우 
        word = '%s' %self.request.POST['word'] 
        # 검색어 
        post_list = Post.objects.filter( Q(title__icontains=word) | Q(content__icontains=word) 
        # Q 객체를 사용해서 검색한다. 
        # title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사 ).distinct() #중복을 제거한다. 
        context = {} 
        context['object_list'] = post_list 
        # 검색된 결과를 컨텍스트 변수에 담는다. 
        context['search_word']= word 
        # 검색어를 컨텍스트 변수에 담는다. 
        
        return context
