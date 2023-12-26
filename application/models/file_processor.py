from abc import ABC, abstractmethod
class FileProcessor(ABC):
    @abstractmethod
    def document_loader(self,file_path):
        pass

    @abstractmethod
    def text_splitter(self,documents):
        pass


    @abstractmethod
    def prepare_vectordb(self,docs,embeddings):
        pass
