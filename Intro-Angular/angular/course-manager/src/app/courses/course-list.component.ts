import { Component, OnInit } from '@angular/core';
import { Course } from './course';
import { CourseService } from './course.service';

@Component({
    templateUrl: './course-list.component.html'
})
export class CourseListComponent implements OnInit { 

    filteredCourses: Course[] = [];

    _courses: Course[] = [];
    
    _filterBy: string;

    constructor(private courseService: CourseService) { }

    ngOnInit(): void {
        this.courses => [
            {
                id: 1,
                name: 'Angular: Forms',
                imageUrl: '/assets/images/forms.png',
                price: 99.99,
                code: 'XPS-9687',
                duration: 120,
                rating: 4.5,
                releaseDate: 'November, 4 2019'
            }
            {
                id: 2,
                name: 'Angular: HTTP',
                imageUrl: '/assets/images/http.png',
                price: 45.99,
                code: 'LKL- 1202',
                duration: 80,
                rating: 4,
                releaseDate: 'November, 4 2019'
            }
        ]
    }
}