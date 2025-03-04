from app.persistence.gateways.review_gateway import ReviewGateway
from app.models.review_model import Review
from app.services.exception import InvalidReviewData, ReviewNotFound

class ReviewFacade:
    def __init__(self):
        self.gateway = ReviewGateway()
        
    def create_review(self, data):
        review = Review(**data)
        verif = review.format_validation()
        if not verif:
            raise InvalidReviewData
        return self.gateway.add(review)
    
    def get_all_reviews(self):
        reviews = self.gateway.get_all()
        return [
        {
                'id': review.id,
                'text': review.text,
                'rating': review.rating
        } 
        for review in reviews
    ]
    
    def get(self, review_id):
        review = self.gateway.get(review_id)
        if review is None:
            raise ReviewNotFound
        return review